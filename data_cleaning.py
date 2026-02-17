import pandas as pd 

# data cleaning= the process of fixing/removing: 
#                incomplete, incorrect, or irrelevant data.
#                ~75% of work done with pandas is data cleaning 

df = pd.read_csv("data.csv")

#1 Drop irrelevant columns 

# df=df.drop(columns=["Legendary","No"])

#2 handle missing data 

# df= df.dropna(subset=["Type2"])
# print(df.to_string()) in toàn bộ 

# replace any values that have types two with none 


# df = df.fillna({"Type2": "None"})


# 3 fix inconsistent values 
# df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
#                                    "Fire":"FIRE",
#                                    "Water":"WATER"})
# print(df.to_string())

# 4 Standardize text

# df["Name"]= df["Name"].str.lower()

#5 fix data types 

# df["Legendary"]= df["Legendary"].astype(bool)

# 6 remove duplicate values 

df = df.drop_duplicates()