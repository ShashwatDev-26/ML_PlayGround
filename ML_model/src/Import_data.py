# This is a class for dummy data of all type 
import os 
from pathlib import Path
import pandas as pd 
import numpy as np 

class dummyData: 
    """
    sample    : int | 10
    n_feature : int | 1
    n_classes : int | 0:clustring, 1:regression, >2: classification
    """
    def __init__(self,sample = 20,n_features = 1,n_classes = 1):
        self.sample      = max(sample,10)
        self.n_features  = max(n_features,1)
        self.n_classes   = max(n_classes,0)
        
        self.independent = np.full((1,),fill_value=False)
        self.dependent   = np.full((1,),fill_value=False)
        self.data_false  = True
    
    def check_data(self):
        if self.independent.any() and self.dependent.any():
            self.data_false = False

    def independent_data(self):
        mu  = 0.01
        std = 0.9
        if self.data_false:
            x = np.random.normal(mu,std, (self.sample,1))
            for i in range(1,self.n_features):
                mu  = mu/i
                temp = np.random.normal(mu,std,(self.sample,1))

                x    = np.hstack((x,temp))
            
            self.independent = np.copy(x)
        self.check_data()
    
    def dependent_data(self):
        if self.data_false:
            if self.n_classes   == 0:
                self.dependent = np.full((self.sample,1),fill_value=-1)
                self.check_data()

            elif self.n_classes == 1:
                self.dependent = np.random.uniform(0.0,1,(self.sample,1))
                self.check_data()
                
            else:
                if self.data_false:
                    self.dependent = np.random.randint(0,self.n_classes,(self.sample,1))
                    self.check_data()

    def export_data(self,name = "sample.csv"):
        if not name.endswith(".csv"):
            name+=".csv"
        if not self.data_false:
            output     = ["Output"]
            featurecol = [f"Feature_{i+1}" for i in range(self.n_features)] + output
            data       = np.hstack((self.independent,self.dependent))
            dataDF     = pd.DataFrame(data,columns=featurecol)
            data_file  = Path(__file__) / ".."/ ".." / "Data"
            Path.mkdir(data_file,exist_ok=True,parents=True)
            csv_file   = str(data_file / name)
            dataDF.to_csv(csv_file,index=False)
            return csv_file,dataDF



          
        







    
if __name__ == "__main__":
    test = dummyData(sample=50,n_features=5,n_classes=0)
    test.independent_data()
    test.dependent_data()
    test.export_data("clustring")