import os
import voiceprint_recognition.Tools.SR_Model as VI_model
global MODEL, MODEL_PATH
directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__))
TEST_FILE = f"{dir_path}/test/test_output.wav"


def setModelPath(modelPath):
    global MODEL_PATH
    # MODEL_PATH = modelPath
    modelpath = open(f"{dir_path}/txtPath/ModelPath.txt", "w")
    modelpath.write(f"{modelPath}/VImodel")
    modelpath.close()
    wordPath = open(f"{dir_path}/txtPath/wordPath.txt", "w")
    wordPath.write(f"{modelPath}/VIwords")
    wordPath.close()


def getModelPath():
    modalPath = open(f"{dir_path}/txtPath/ModelPath.txt", "r")
    readModalPath = modalPath.read()
    modalPath.close()
    return readModalPath


def getAccuracyFilePath():
    """
    Returns:
        the accuracy file path of current recorded with microphone
    """
    return f"{getModelPath()}//m_accuracy.txt"


def getWordPath():
    wordPath = open(f"{dir_path}/txtPath/wordPath.txt", "r")
    word = wordPath.read()
    wordPath.close()
    return word


def getPath():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path


def getTestWaveFile():
    """
    returns the predicted recorded file path.
    Returns:
        the predicted recorded file path.
    """
    return f"{getPath()}\\test\\test_output.wav"


def loadModel():
    """
    returns the saved model in the container
    Returns:
        the saved model in the container
    """
    return SR_Model.loadModel()


def userNames():
    """
    returns the name of users in a list formate
    Returns:
        the name of users in a list formate
    """
    return os.listdir(f"{getWordPath()}\\sentence\\")

def userCount():
    """
    returns the no of users that has been stored
    Returns:
        the no of users that has been stored
    """
    return len(os.listdir(f"{getWordPath()}\\sentence\\"))

