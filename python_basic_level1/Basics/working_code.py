import pandas as pd

d1={"name":["Mahesh","Ramesh","Mahesh"], "id":[1,2,2],"received_datetime":
    ["2025-10-02","2025-01-10","2025-01-11"], "marks":[90, 100, 120]}
print(d1)
d2=pd.DataFrame(d1)
d2["received_datetime"]=pd.to_datetime(d2["received_datetime"])
print(d2.head())
d3=d2["received_datetime"].dt.year.unique().tolist()
print(d3)
d4=d2["marks"].sum()
print("The sum is ",d4)
d5=d2.groupby("name")["marks"].sum()
print(d5)
d2["year"]=d2["received_datetime"].dt.day_name()
d2.drop(columns=["year","marks"], inplace =True)
d2.index=["A","B","C"]
print(d2.reset_index(inplace=True))
d2.sort_values(["name"], inplace=True)
d1=d2[d2["name"].str.startswith("M")]
print(d1)