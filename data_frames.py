import pandas as pd 

data = {"Name": ["Spongebob", "Patrick", "Squidwards"],

         "Age": [30,35,50]
}

df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])

# add a new column 

df ["job"] = ["Chef", "Manager","Cashier"]

# add a new row 

new_row = pd.DataFrame([{"Name": "Lucy", "Age": 16, "job": "CEO"}, 
                       {"Name": "Linhuan", "Age": 17, "job": "HR Manager"}], 

                          index=["Employee 4", "Employee 5"])

# thêm row vào dataframe

df = pd.concat([df, new_row])

# print(df.loc["Employee 1"])

# print(df.iloc[0])

print (df)