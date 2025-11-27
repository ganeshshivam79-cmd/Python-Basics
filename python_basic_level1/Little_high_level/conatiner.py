class MyDict:
    def __init__(self):
        self.data = {}  # internal storage

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __str__(self):
        return str(self.data)


# Create object
obj = MyDict()

# Set values
obj['name'] = "Mahesh"
obj['age'] = 25
obj['city'] = "Chennai"

print(obj)         # {'name': 'Mahesh', 'age': 25, 'city': 'Chennai'}

# Get values
print(obj['name'])  # Mahesh

# Delete a key
del obj['age']
print(obj)          # {'name': 'Mahesh', 'city': 'Chennai'}
