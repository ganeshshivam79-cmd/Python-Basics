# Define the generator function
def generator():
    for num in range(3):
        yield num  # produces numbers one by one

# Create a generator object
key1 = generator()

# Access values using next()
print("Using next():")
print(next(key1))  # Output: 0
print(next(key1))  # Output: 1
print(next(key1))  # Output: 2

# Once exhausted, next() would raise StopIteration
# print(next(key1))  # Uncommenting this line would raise StopIteration

# Re-create the generator to iterate again
key1 = generator()

# Access values using a for loop
print("\nUsing for loop:")
for val in key1:
    print(val)

# Example: Using generator in a list comprehension
key2 = generator()
squared = [x**2 for x in key2]
print("\nSquared values:", squared)
