import pandas as pd 

df = pd.read_csv("data.csv")

# filtering = keeping the rows that match a condition 

# tall_pokemon= df[df["Height"]>= 2]

# print(tall_pokemon)


# legendary_pokemon = df[df["Legendary"] == True]

# print (legendary_pokemon)


# water_pokemon= df[(df["Type1"] == "Water")|
#                   (df["Type2"] == "Water")]

# print(water_pokemon)


# ff_pokemon= df[(df["Type1"]=="Fire")&
#                (df["Type2"]=="Flying")]

# print(ff_pokemon)
