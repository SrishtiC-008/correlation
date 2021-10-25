import csv
import numpy as np 

def getDataSource(data_path):
    temperature = []
    ice = []
   
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            temperature.append(float(row["Temperature"]))
            ice.append(float(row["Ice"]))
            

    return {"x" : temperature, "y" : ice} 

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Icecream and Temperature:- \n--->",correlation[0,1])

def setup():
    data_path = "./Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()









