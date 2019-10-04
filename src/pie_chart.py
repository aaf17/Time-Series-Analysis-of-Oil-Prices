#import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import random as rd 

#read the csv file
root_folder = "./src/new_data"
df = pd.read_csv(root_folder+"/"+ "new.PMO.L.csv")
df = df[['High']]

name= ["From 140 to 160", "From 120 to 139", "From 100 to 119", "From 80 to 99", "From 60 to 79"]

x1 = len(df[(df.High>=140)&(df.High<160)])
x2 = len(df[(df.High>=120) & (df.High<140)])
x3 = len(df[(df.High>=100) & (df.High<120)])
x4 = len(df[(df.High>=80) & (df.High<100)])
x5 = len(df[(df.High>=60) & (df.High<80)])

values = [x1, x2, x3, x4, x5]

plt.axis("equal")
plt.pie(values, labels=name, radius=1.15, autopct='%0.0f%%', shadow=True,  explode=[0,0,0,0,0.1], startangle=360)
plt.title("Highest Share Price value Pie Chart for Premier Oil (PMO)", color="black")
plt.savefig("./plots/pie_chart.png", format="png")
plt.show(block=False)
plt.pause(8)