import pandas as pd
import csv
df = pd.read_csv("final_data.csv")
# changing masses , radiuses to float and converting to si mass , si radius''
mass_list = []
radius_list = []
for i in df["Mass"]:
    i = float(i)
    i = i*1.989e+30
    mass_list.append(i)
for i in df["Radius"]:
    i = float(i)
    i = i*6.957e+8
    radius_list.append(i)
gravity_list = [] 
for index, mass in enumerate(mass_list): 
  gravity = (mass_list[index])* 6.674e-11  / (radius_list[index]*radius_list[index]) 
  gravity_list.append(gravity) 
df["gravity"] = gravity_list
print(df)