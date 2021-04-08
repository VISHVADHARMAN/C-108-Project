import plotly.figure_factory as ff 
import pandas as pd 
import csv

df=pd.read_csv("D:/C-108/C-108 Project/mobile brand.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"])
fig.show()