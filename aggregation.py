import pandas as pd 

# aggregate functions = reduces a set of values into a single summary value 
#                      Used to summarise and analyse data
#                      often used with the groupby() function

df = pd.read_csv("data.csv")

#whole dataframe
# print(df.mean(numeric_only=True))

# print(df.sum(numeric_only=True))


# print(df.max(numeric_only=True))

# print(df.min(numeric_only=True))

# print(df.count())


#single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())
# print(df["Type2"].count())

group=df.groupby("Type1")

# print(group["Height"].mean())

# print(group["Height"].sum())
# print(group["Height"].max())
# print(group["Height"].min())
# print(group["Height"].count())