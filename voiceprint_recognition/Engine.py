import os
import shutil
from voiceprint_recognition.Tools import Data
from voiceprint_recognition.Tools import SR_Model
from voiceprint_recognition.Tools import Predictor
import voiceprint_recognition.Container as Container
import time
import warnings
import tensorflow as tf
import logging
global saveModelPath, loadModelPath, accuracyPath
directory_to_project = dir_path = os.path.dirname(os.path.realpath(__file__))

def start(getDIR):
    """Used to create a personal space for your file
    When we have to work on two different schemas of work..
    there is a confusion in them for the Compiler , Engine.Start() plays a vital role in sorting on the different
    projects by preloading in them when needed automatically.

    Short : Engine is used for taking up the directive to work with different projects at the same time
    when working we must pass the directive as parameter in the engine to take up the path to work in it

    """
    tf.get_logger().setLevel(logging.ERROR)
    warnings.filterwarnings("ignore")
    Container.setModelPath(getDIR)
    if not os.path.exists(Container.getModelPath()):
        # os.makedirs("model")
        source_dir = directory_to_project+"/model"
        destination_dir = Container.getModelPath()
        Container.MODEL_PATH = Container.getModelPath()
        shutil.copytree(source_dir, destination_dir)
    if not os.path.exists(Container.getWordPath()):
        source_dir = dir_path+"/words"
        destination_dir = Container.getWordPath()
        shutil.copytree(source_dir, destination_dir)
    Data.names = os.listdir(f"{Container.getWordPath()}\\sentence")
    try:
        SR_Model.DIR_MODEL = f"{Container.getModelPath()}\\saved_model"
        SR_Model.ACCURACY_TEXT_FILE = f"{Container.getModelPath()}\\saved_model\\m_accuracy.txt"
    except NameError:
        print("saveModelPath is not defined\nPlease set Model Name\nHelp --> You have to ")
    # Container.MODEL = SR_Model.loadModel()
    Predictor.WAVE_OUTPUT_FILENAME = f"{dir_path}/test/test_output.wav"  # testing file
    print("Engine Started...")
    time.sleep(2)

# start()