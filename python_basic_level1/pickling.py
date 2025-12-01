"""
Pickling is the process of converting a Python object hierarchy into a byte stream.
This byte stream can then be: Stored in a file, Transmitted over a network, and Stored in a 
database

Unpickling is the inverse process of converting a pickled byte stream back into a Python object
hierarchy. 

"""

import pickle

# Data to save
data = {"name": "Shivam", "age": 27, "skills": ["Python", "AWS"]}

# Save object to file (Pickling)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load object back (Unpickling)
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
