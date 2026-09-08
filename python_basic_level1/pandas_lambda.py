df["age"]=df.apply(lambda x: 18 if x["name"]=="Jack" and x["marks"]>90 else x["age"], axis=1)
