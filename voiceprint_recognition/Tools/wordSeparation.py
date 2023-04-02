from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import os
import shutil
from playsound import playsound
from voiceprint_recognition import Container

directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__))


def clearAudio(path):

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def separateWords(sound_file_name):

    sound_file = AudioSegment.from_wav(sound_file_name)

    audio_chunks = split_on_silence(sound_file, min_silence_len=50, silence_thresh=(int(sound_file.dBFS) - 10))

    clearAudio(f"{Container.getPath()}/splitAudio")
    out_files = []
    for i, chunk in enumerate(audio_chunks):
        if chunk.dBFS > -70: # only write file if volume is above silence threshold
            out_file = f"{Container.getPath()}/splitAudio//chunk{i}.wav"
            out_files.append(out_file)
            # print("Exporting", out_file) # Check to see exporting
            chunk.export(out_file, format="wav")

    return out_files