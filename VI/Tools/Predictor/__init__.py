import os
import pandas as pd
import librosa
from sklearn.model_selection import train_test_split
import numpy as np
import pyaudio
import wave
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from voice_identification.Tools import wordSeparation
from voice_identification import Container
import csv
N_MFCCS = 24  # number of MFCCs to use in feature extraction

global WAVE_OUTPUT_FILENAME


def getDataFromDir(dir):

    try:
        speakers = os.listdir(dir)
        speakers = speakers[:10]

        df = pd.DataFrame(columns=['filepath', 'speaker'])
        for speaker in speakers:
            files = os.listdir(dir + '{}/'.format(speaker))
            for file in files:
                filepath = dir + '{}/{}'.format(speaker, file)
                df = df.append({'filepath': filepath, 'speaker': speaker}, ignore_index=True)
        return df
    except Exception as E:
        print(E)


def extractFeatures(filename, n_mfccs=N_MFCCS):
    """
    This function used to extract and return the audio features

    Args:
        filename:
        n_mfccs:

    Returns:

    """

    X, sample_rate = librosa.load(filename, res_type='kaiser_fast')

    mfccs = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=n_mfccs)
    mfccs_mean = np.mean(mfccs.T, axis=0)

    # print(X)
    # print(sample_rate)
    # print(mfccs)

    csvFileName = "mfcc_Future.csv"
    rowEnter = ''
    for i in mfccs_mean:
        rowEnter = rowEnter + " " + str(i)
    rowEnter = rowEnter.split()

    writefile = open(csvFileName, "a", newline='')
    writer = csv.writer(writefile)
    writer.writerow(rowEnter)
    # print(rowEnter)
    rowEnter = ''
    #
    # delta = librosa.feature.delta(mfccs)
    # delta_mean = np.mean(delta.T, axis=0)
    #
    # deltadelta = librosa.feature.delta(mfccs, order=2)
    # deltadelta_mean = np.mean(deltadelta.T, axis=0)

    return mfccs_mean.tolist()#  + delta_mean.tolist() + deltadelta_mean.tolist()


def getFeatures(filepaths, ss):

    features = filepaths.apply(extractFeatures)
    features = features.tolist()
    features_scaled = ss.fit_transform(features)
    return features_scaled


def getEncodedLabels(speaker_names):

    speaker_names.tolist()
    lb = LabelEncoder()
    return to_categorical(lb.fit_transform(speaker_names))


def predictSpeaker(file_path, word_model):
    """
    we pass the audio file and  model as parameter and
    Extract feature in live voice and compare the feature with saved feature and
    This function returns the username and accuracy as a list.

    Args:
        file_path:
        word_model:

    Returns:

    """

    labels = word_model.train_labels_encoded.tolist()  # list of the encoded labels from training
    # print(labels)

    features = word_model.ss.transform([extractFeatures(file_path)])

    to_predict = np.array(features)  # list of data for the model to predict, just one item for now

    predictions = word_model.model.predict(to_predict)  # returns a list of predictions
    pred = predictions[0].tolist()  # take the first element which is the prediciton for the first element in to_predict, remember this is still one hot encoded so it is a big array of 0s and 1s
    # print("2", predictions)
    # print(pred)
    m = max(pred)
    # print(m)
    p = [1 if i == m else 0 for i in pred]  # convert highest propability to 1 and all else to 0
    # print(p)
    try:
        prediction_ind = labels.index(p)  # index of predicted label (encoded)
        prediction = word_model.train_labels[prediction_ind]
        # print(prediction)
        # print(prediction_ind)

    except Exception as E:
        prediction = "could not identify speaker"

    return prediction, m

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def getInputFromMic():
    global WAVE_OUTPUT_FILENAME
    RECORD_SECONDS = 1

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("say '' in: 2")
    for i in range(1, 0, -1):
        time.sleep(1)
        print(i)
    time.sleep(1)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(Container.getTestWaveFile(), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return Container.getTestWaveFile()


def getMeetingInput(secs = 2):
    global WAVE_OUTPUT_FILENAME
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # select the name of the audio input you want to use! see readme for details
        if (dev['name'] == 'Microphone (Realtek(R) Audio)' and dev['hostApi'] == 0):
            dev_index = dev['index']

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=48000,
                    input=True,
                    input_device_index=dev_index,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * secs)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(Container.getTestWaveFile(), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return Container.getTestWaveFile()


def mostFrequent(p, c):

    if len(p) == 0:
        return '', 0

    confs = {}
    counts = {}
    for i in range(len(p)):
        confs[p[i]] = confs.get(p[i], 0) + c[i]
        counts[p[i]] = counts.get(p[i], 0) + 1

    speaker = max(confs, key=confs.get)
    confidence = confs[speaker]/counts[speaker]
    return speaker, confidence


def predict(model, s=2):
    """
    The load model is passed as parameter to this predict function and triggers microphone for 2 second and
    Extract feature in live voice and compare the feature with saved feature and
    This function Returns the username and accuracy as a list.

    Args:
        model:
        s:

    Returns:

    """
    print("Speak...")
    one_second_input = getMeetingInput(s)
    chunks = wordSeparation.separateWords(one_second_input)

    predictions = []
    confidence = []
    for chunk in chunks:
        try:
            pred, c = predictSpeaker(chunk, model)

            # print(f"{pred}, {c}")
            predictions.append(pred)
            confidence.append(c)
        except:
            pass
    pre, con = mostFrequent(predictions, confidence)
    if con > 0.85:
        return pre, con
    else:
        return "No one Speak", 0


def liveInput(model):

    while True:
        print(predict(model, 2))

# while True:
#     print(predict(Container.getModelPath()))