import numpy as np
import plotly.express as px
import pandas as pd
import csv

reader_csv = csv.DictReader("MARKS-DAYS.py")
df = pd.read_csv(reader_csv)
fig = px.scatter(df, x="Coffee In mL", y="SleepTime in Hours",
	        size="Percentage",color="Country",
            size_max=60)
fig.show()

def DataSource(data_path):
    days=[]
    marks=[]

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            marks.append(float(row["Marks"]))
            days.append(float(row["Days Present"]))
    
    return {"x" : days, "y" : marks}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation Is -->", correlation[0,1])

def setup():
    data_path = "MARKS-DAYS.csv"
    data_source = DataSource(data_path)
    findCorrelation(data_source)

setup()
