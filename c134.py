from matplotlib.cbook import to_filehandle
import pandas as pd 

df = pd.read_csv("calculated.csv")
distance = df["Distance"].tolist()
gravity = df["Gravity"].tolist()
radius = df["Radius"].tolist()
mass = df["Mass"].tolist()
new_gravity = []
new_distance = []
new_radius = []
new_mass = []

for i in range(0,len(distance)) :
    if float(gravity[i]) >= 150 and  float(gravity[i]) <= 350 and float(distance[i]) <= 100 :
        new_distance.append(distance[i])
        new_gravity.append(gravity[i])
        new_radius.append(radius[i])
        new_mass.append(mass[i])

""" print(new_distance)
print(new_gravity)
print(new_radius)
print(new_mass) """

newdf = pd.DataFrame({"Distance" : new_distance, "Mass" : new_mass, "Radius" : new_radius, "Gravity" : new_gravity})
newdf.to_csv("criteria.csv")
    



