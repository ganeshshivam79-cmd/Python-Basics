"""select only even index"""
df.iloc[1::2]


"""odd index"""
df.iloc[1::2]

"""index or value"""
df_selected = df[df.index.to_series().str.startswith("a")]
df = df[df["name"].str.startswith(('A','a'))]


"dictionary into Dataframe"
data = {
    'row1': {'id': 1, 'name': 'A', 'age': 25},
    'row2': {'id': 2, 'name': 'B', 'age': 30},
}
df = pd.DataFrame.from_dict(data, orient='index')