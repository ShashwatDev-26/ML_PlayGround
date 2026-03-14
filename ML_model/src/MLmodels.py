import os 
from pathlib import Path
import joblib
import numpy as np  
import pandas as pd
from Import_data import dummyData

# preprocessing 
from sklearn.model_selection import train_test_split,cross_val_score

# Regression 
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Clustring
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture




class modelSelection(dummyData):
    def __init__(self,file_name="sample.csv"):
        super().__init__()
        self.BASE_PATH   = Path(__file__).absolute().parent /".."
        self.file_name   = file_name
        self.file_path   = "-1"
        self.file_valid  = False
        self.DataDF      = None
        self.models_     = ["Regression","Classification","Clustring"]
        self.model_type  = None
        self.ML_model    = None
        
    def file_and_data(self):
        if not self.file_name.endswith(".csv"):
            self.file_name += ".csv"
        self.file_path = os.path.join(os.path.dirname(__file__),"..","Data",self.file_name)
        if os.path.exists(self.file_path):
            self.file_valid = True
            
    def import_Data(self):
        if self.file_valid:
            self.DataDF      = pd.read_csv(self.file_path)
            self.independent = self.DataDF.iloc[:,:-1].values
            self.dependent   = self.DataDF.iloc[:,-1:].values
            super().check_data()
        else:
            print("[*] no data in-line")
            exit()
    
    def model_recognization(self,sample_size = 12):
        sample = self.dependent[:sample_size]
        Ucount = len(np.unique(sample))

        if np.all(sample == -1):
            self.model_type = self.models_[-1]
        elif Ucount > sample_size-1:
            self.model_type = self.models_[0]
        else:
            self.model_type = self.models_[1]

    def model_select(self):
        modelAddress = self.BASE_PATH / "saved_model" / self.model_type
        if modelAddress.is_dir():
            pass
        else:
            modelAddress.mkdir(parents=True,exist_ok=True)
        models_list = {"test.joblib":LinearRegression()}
        if self.model_type == self.models_[0]:
            # regression
            models_list = {
                "SVR.joblib"                 : SVR(),
                "Linear_Regression.joblib"   : LinearRegression(),
                "KNeighborsRegressor.joblib" : KNeighborsRegressor(),
                "DicisionTreeReg.joblib"     : DecisionTreeRegressor()
                }

        elif self.model_type == self.models_[1]:
            # classification
            models_list = {
                "SVC.joblib"                : SVC(),
                "Logistic_Regression.joblib": LogisticRegression(),
                "KNeighborsClf.joblib"      : KNeighborsClassifier(),
                "DecisionTreeClf.joblib"    : DecisionTreeClassifier()       
                }
        elif self.model_type == self.models_[2]:
            # clustring
            models_list = {
                "KMeans.joblib"          : KMeans(),
                "DBSCAN.joblib"          : DBSCAN(),
                "GaussianMixture.joblib" : GaussianMixture()
                }

        for key,model in models_list.items():
                fileaddress = modelAddress / key 
                joblib.dump(model,fileaddress)
        
class ModelTraining:
    def __init__(self,model):
        self.model = model
    def parameterExtrection(self):
        print(self.model.get_params())

    


        

        


if __name__ == "__main__":
    # test = modelSelection("Loan_defaulter")
    # test.file_and_data()
    # test.import_Data()
    # test.model_recognization()
    # test.model_select()
    test = ModelTraining(DecisionTreeClassifier())
    test.parameterExtrection()






