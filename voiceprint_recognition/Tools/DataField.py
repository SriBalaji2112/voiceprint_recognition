from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import wave
import os
from playsound import playsound
import pyaudio
from time import sleep
import shutil
from voiceprint_recognition.Tools.wordSeparation import clearAudio
from voiceprint_recognition import Container


directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__))  # "C:\\Users\\harle\\PycharmProjects\\QMINDv4"

# What do you want the program to do?
# newDataRecorder = False  # Records all data from your microphone
# splitAudioOnSilence = False  # Breaks up the recorded data to separate audio files
# play_recordings = True  # Plays you broken up audio files!


def createRecordDATA(directory, seconds):
    """
    Helper function to record audio (Actually records it and places into collected recordings)
    Args:
        directory: str
            The word that the person is saying multiple times
        seconds: int
            Amount of time given to record. (Usually 7-8 seconds)
    """
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    filename = f"{Container.getPath()}\\collectedRecordings\\rawRecordings\\{directory}_RecordedData.wav"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    # print("Say \"" + directory + "\" 5 times in 3")
    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


sound_file_name = "RecordedData.wav"
# These are the words used. If you want to add/delete them MAKE sure to add/delete the directory before
directories = ["the", "of", "and", "to", "be"]


def newDataRecorder():
    """
    Records all new data by calling the create recorded data function for each word we are training on
    """
    print("Prepare your audio recording device. ")
    print("Wait 0.5 seconds in between each word you say. ")
    print("You have eight seconds for each; once you have spoken five times, remain silent.")
    sleep(5)
    for directory in directories:
        createRecordDATA(directory, 8)


def record_sentence(name, s=10):
    print("\nPrepare your audio recording device.  \n")
    sleep(2)
    print(f"You have {s} seconds to read the passage below.  \n")
    sleep(2)
    print('"That quick beige fox jumped in the air over each thin dog. Look out, I shout, for he\'s foiled you again, creating chaos"\n')
    sleep(1)
    print("recording in 3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)

    createRecordDATA("sentence", s)

    splitAudioOnSilence(["sentence"])

    exportRecordings(name, ["sentence"])


def splitAudioFileOnSilence():
    audioFile = open(f"{Container.getPath()}/txtPath/audioPath.txt", "r")
    file = audioFile.read()
    audioFile.close()
    sound_file = AudioSegment.from_wav(file)
    # min_silence_len=time in milliseconds, silence_thresh=what the comp classifies as silence in dB
    audio_chunks = split_on_silence(sound_file, min_silence_len=100, silence_thresh=(int(sound_file.dBFS) - 10),
                                    keep_silence=100)

    clearAudio(f"{Container.getPath()}\\collectedRecordings\\sentence")
    numWords = 0

    for i, chunk in enumerate(audio_chunks):
        out_file = f"{Container.getPath()}\\collectedRecordings\\sentence\\{i + 1}.wav"
        # print("Exporting", out_file) # Check to see exporting
        chunk.export(out_file, format="wav")

        numWords += 1
    print(f"Exported {numWords} .wav files")
    print("Please wait your Audio Extracting...")

    audioTOtextSeparator(f"{Container.getPath()}\\collectedRecordings\\rawRecordings\\sentence_RecordedData.wav")  # converts audio to text


def splitAudioOnSilence(dirs= directories):  # Break up the audio into separate word files

    for directory in dirs:
        sound_file = AudioSegment.from_wav(f"{Container.getPath()}\\collectedRecordings\\rawRecordings\\{directory}_RecordedData.wav")
        # min_silence_len=time in milliseconds, silence_thresh=what the comp classifies as silence in dB
        audio_chunks = split_on_silence(sound_file, min_silence_len=100, silence_thresh=(int(sound_file.dBFS) - 10), keep_silence=100)

        clearAudio(f"{Container.getPath()}\\collectedRecordings\\{directory}")
        numWords = 0

        for i, chunk in enumerate(audio_chunks):

            out_file = f"{Container.getPath()}\\collectedRecordings\\{directory}\\{i+1}.wav"
            # print("Exporting", out_file) # Check to see exporting
            chunk.export(out_file, format="wav")
            numWords += 1
        print(f"Exported {numWords} .wav files")
        print("Please wait your Audio Extracting...")

        audioTOtextSeparator(f"{Container.getPath()}\\collectedRecordings\\rawRecordings\\{directory}_RecordedData.wav")  # converts audio to text


def audioTOtextSeparator(audio_dir):

    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(audio_dir) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text

def exportAudioFill(name):
    numFiles = os.listdir(f"{Container.getPath()}\\collectedRecordings\\sentence")
    for file in range(1, len(numFiles) + 1):
        src = f"{Container.getPath()}\\collectedRecordings\\sentence\\{file}.wav"
        dst = f"{Container.getWordPath()}\\sentence\\{name}\\{file}.wav"
        if not os.path.isdir(f"{Container.getWordPath()}\\sentence\\{name}"):
            os.mkdir(f"{Container.getWordPath()}\\sentence\\{name}")
        shutil.copy(src, dst)


def exportRecordings(name, dirs=directories):

    for directory in dirs:
        numFiles = os.listdir(f"{Container.getPath()}\\collectedRecordings\\{directory}")
        for file in range(1,len(numFiles)+1):
            src = f"{Container.getPath()}\\collectedRecordings\\{directory}\\{file}.wav"
            dst = f"{Container.getWordPath()}\\{directory}\\{name}\\{file}.wav"
            if not os.path.isdir(f"{Container.getWordPath()}\\{directory}\\{name}"):
                os.mkdir(f"{Container.getWordPath()}\\{directory}\\{name}")
            shutil.copy(src, dst)
            # print(f"copied {src} to {dst}")


def record_and_save(name):

    newDataRecorder()
    splitAudioOnSilence()
    # play_recordings()
    exportRecordings(name)
