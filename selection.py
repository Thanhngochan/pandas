import pandas as pd 

# df = pd.read_csv("data.csv")

# df = pd.read_csv("data.csv",index_col="Name")

#selection by column

# print(df["Height"].to_string())


# print(df[["Name","Height","Weight"]].to_string())

# select by rows 

# print(df.loc[0])


# print(df.loc["Pikachu"])

# print(df.loc["Charizard",["Height","Weight"]])

# giới hạn từ bao nhiêu tới bao nhiêu rows [0:11]
# print(df.iloc[0:11]) 


# lấy row với số chẵn hoặc lẻ giới hạn lại 3 column
# print (df.iloc[0:11:2,0:3])


df=pd.read_csv("data.csv",index_col="Name")

pokemon = input("Enter a Pokemon name:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
    



