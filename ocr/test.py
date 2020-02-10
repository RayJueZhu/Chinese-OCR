import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
modelPath = os.path.join(os.getcwd(), "my_model_keras.h5")
print(parentdir)
print(modelPath)
print(os.getcwd())
print(os.path.exists(modelPath))