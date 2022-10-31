import model
import cv2
from pathlib import Path
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.text import Text

# import pypokedex

class Predict:

    def __init__(self, img_path: str):
        self.img_path = img_path

    def predict(self):

        img = cv2.imread(self.imgpath)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = img/255
        img = cv2.resize(img, (50,50))

        mymodel = model.Model()
        self.pred_pokemon = unique_names[mymodel.model.predict([img])] 

    def pokemon_info(self):

        self.predict()
        df = pd.read_csv("C:\\Users\\HP\\Desktop\\AI Projects\\Pokedex\\pokedex.csv")
        df1 = df[df['name'] == self.pred_pokemon]

        l1_type1 = str(df1["type1"]).split()
        l1_type2 = str(df1["type2"]).split()
        l1_ability1 = str(df1["ability1"]).split()
        l1_ability2 = str(df1["ability2"]).split()
        l1_dex = str(df1["dex"]).split()
        l1_height = str(df1["height"]).split()
        l1_weight = str(df1["weight"]).split()
        l1_mega_evolve = str(df1["mega_evolve"]).split()
        self.type1 = l1_type1[1]
        self.type2 = l1_type2[1]
        self.ability1 = l1_ability1[1]
        self.ability2 = l1_ability2[1]
        self.dex = l1_dex[1]
        self.height = l1_height[1]
        self.weight = l1_weight[1]
        self.mega_evolve = True if l1_mega_evolve[1] == "True" else False

        text = Text(
        "Pokedex",
        justify="center",
        style="bold underline #D10000 on #FFF5EE")

        table = Table()

        table.add_column("dex", style="cyan", no_wrap=True)
        table.add_column("Pokemon", style="magenta")
        table.add_column("Type1", justify="right", style="green")
        table.add_column("Type2", justify="right", style="orange")
        table.add_column("Ability1", justify="right", style="red")
        table.add_column("Ability2", justify="right", style="yellow")
        table.add_column("Height", justify="right", style="blue")
        table.add_column("Weight", justify="right", style="green")
        table.add_column("Mega Evolve", justify="right")

        if self.mega_evolve:
            table.add_row(self.dex, self.pred_pokemon, self.type1, self.type2, self.ability1, self.ability2, self.height, self.weight, "✅")
        elif not self.mega_evolve:
            table.add_row(self.dex, self.pred_pokemon, self.type1, self.type2, self.ability1, self.ability2, self.height, self.weight, "❌")

        console = Console()
        console.print(table)


if __name__ == "__main__":

    img_path = Path(input("Enter the full path to the image file: "))
    if not path.exists():
        print("The path to the file you gave is incorrect/doesn't exist.")
        quit(1)
    
    pokemon = Predict(img_path)
    pokemon.pokemon_info()




