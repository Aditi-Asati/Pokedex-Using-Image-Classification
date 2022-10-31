import os, random
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import cv2

class Model:

    def __init__(self):
        """
        Constructor 
        """
        self.img_folder_dir = "C:\\Users\\HP\\Desktop\\AI Projects\\Gen 1 Pokedex\\pokemon_images"
        self.x_train = np.array([])
        self.all_names = []
        self.y_train = []

        self.create_features()
        self.create_labels()
        self.train_model()

    def create_features(self):
        """
        Creates features for the training data from the pokemon images 
        """
        for imgpath in os.listdir(self.img_folder_dir):
            pokemon_name = imgpath.split(".")[0].split("_")[0]
            self.all_names.append(pokemon_name)
            img = cv2.imread(os.path.join(self.img_folder_dir, imgpath))
            
            # 96*96*3 - dimension of each image
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # img.shape - 96*96
            img = img/255
            img = cv2.resize(img, (50,50))
            # img.shape = 50*50
            self.x_train = np.append(self.x_train, [img])
            
        self.x_train = self.x_train.reshape(690, 2500)

    def create_labels(self):
        """
        Creating labels for the training data
        """
        unique_names = []
        label = 0
        for i in range(len(self.all_names)):
            if i == 0:
                self.y_train.append(label)
                unique_names.append(self.all_names[i])
                continue
            if self.all_names[i] != self.all_names[i-1]:
                unique_names.append(self.all_names[i])
                label += 1
                self.y_train.append(label)
            else:
                self.y_train.append(label)
                
        self.y_train = np.array(self.y_train)

    def train_model(self):
        """
        Training the Random Forest Classifier model
        """
        self.model = RandomForestClassifier(n_estimators = 4, n_jobs=-1)
        self.model.fit(self.x_train, self.y_train)



