import model
import cv2
from pathlib import Path
import pandas as pd
# import pypokedex

class Predict:

    def __init__(self):
        pass

    def predict(self, img_path: str):

        img = cv2.imread(imgpath)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = img/255
        img = cv2.resize(img, (50,50))
        self.pred_pokemon = unique_names[model.predict(img)] 

    def pokemon_info(self):

        df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI Projects\\Pokedex\\pokedex.csv")
        

if __name__ == "__main__":

    img_path = Path(input("Enter the full path to the image file: "))
    if not path.exists():
        print("The path to the file you gave is incorrect/doesn't exist.")
        quit(1)
    




