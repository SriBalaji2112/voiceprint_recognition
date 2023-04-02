from voiceprint_recognition import Engine
from voiceprint_recognition.Tools import Data, Predictor, SR_Model
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
Engine.start(dir_path)

Data.addUserName("BalajiSanthanam")
Data.recordNewAudio()

SR_Model.trainModel()
model = SR_Model.loadModel()

print(Predictor.predict(model))
# Data.deleteUser("BalajiSanthanam")
