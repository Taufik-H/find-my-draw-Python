from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import numpy as np
import os

def load_dataset():
    satu = []
    dua = []
    tiga = []

    for file in os.listdir("satu"):
        img = Image.open("satu/"+file)
        img = np.array(img)
        img = img.flatten()
        satu.append(img)

    for file in os.listdir("dua"):
        img = Image.open("dua/"+file)
        img = np.array(img)
        img = img.flatten()
        dua.append(img)
    
    for file in os.listdir("tiga"):
        img = Image.open("tiga/"+file)
        img = np.array(img)
        img = img.flatten()
        tiga.append(img)
    return satu, dua, tiga
def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    satu, dua, tiga = load_dataset()
    print("[INFO] Loading Model")
    y_satu =np.zeros(len(satu))
    y_dua = np.ones(len(dua))
    y_tiga = np.ones(len(tiga))*2
    x = satu + dua + tiga
    y = np.concatenate([y_satu, y_dua, y_tiga])
    model.fit(x, y)
    return model
