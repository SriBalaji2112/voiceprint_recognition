from voice_identification.Tools.VoiceClassifier import *
from voice_identification import Container

global MODEL, ACCURACY, STATUS, DIR_MODEL, ACCURACY_TEXT_FILE


def loadModel():
    """
    This function returns the saved model.

    Returns:

    """
    global STATUS
    DIR_MODEL = f"{Container.getModelPath()}\\saved_model"
    try:
        global MODEL
        MODEL = word_model(['sentence'], load=True, path=DIR_MODEL)
        STATUS = 1
        return MODEL
    except:
        STATUS = 0


def saveAccu():
    """
    This function used to save the accuracy of the recorded audio, Audio accuracy ranges from 0 to 1 rounding up to
    4 decimals, Accuracy is said to perfect when frequency is 0.99 to 1 if low accuracy re-recording is a very good
    choice for good qualitative result..

    Returns:

    """
    global ACCURACY
    f = open(Container.getAccuracyFilePath(), "w")
    acc_str = str(round(ACCURACY, 3))
    f.write(acc_str)
    f.close()
    loadModel()


def saveModel():
    """
    Saves the recorded feature model in a database.

    Returns:

    """
    global MODEL, DIR_MODEL
    DIR_MODEL = f"{Container.getModelPath()}\\saved_model"
    try:
        MODEL
    except NameError:
        print("Model Not Trained :(")
        return 0
    MODEL.model.save(DIR_MODEL)
    saveAccu()


def trainModel():
    """
    This function used to extract the voice feature of the recorded audio and pass the trained model as parameter to the
    saveModel()

    Returns:

    """
    global MODEL, ACCURACY
    MODEL = word_model(['sentence'])
    ACCURACY = MODEL.accuracy[-1]
    saveModel()
