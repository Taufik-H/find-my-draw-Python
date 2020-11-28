from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import numpy as np
import os

def load_dataset():
    angry = []
    sad = []
    smile = []

    for file in os.listdir("angry"):
        img = Image.open("angry/"+file)
        img = np.array(img)
        img = img.flatten()
        angry.append(img)

    for file in os.listdir("sad"):
        img = Image.open("sad/"+file)
        img = np.array(img)
        img = img.flatten()
        sad.append(img)
    
    for file in os.listdir("smile"):
        img = Image.open("smile/"+file)
        img = np.array(img)
        img = img.flatten()
        smile.append(img)
    return angry, sad, smile
def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    angry, sad, smile = load_dataset()
    print("[INFO] Loading Model")
    y_angry =np.zeros(len(angry))
    y_sad = np.ones(len(sad))
    y_smile = np.ones(len(smile))*2
    x = angry + sad + smile
    y = np.concatenate([y_angry, y_sad, y_smile])
    model.fit(x, y)
    return model
