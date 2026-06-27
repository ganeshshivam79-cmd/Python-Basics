df = df.drop_duplicates()

df = df.drop_duplicates(subset=['id'])


df = df.drop_duplicates(
    subset=["name"],
    keep="last"
)

df = df.drop_duplicates(
    subset=["name"],
    keep=False
)
dont keep any repeated values

df = df.drop_duplicates(keep="last")