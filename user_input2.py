# Initialize an empty dictionary
person_info = {}

# Get user input for name, age, and favorite color
name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter your location: ")

# Store the inputs in the dictionary
person_info['name'] = name
person_info['age'] = age
person_info['location'] = location

# Print the dictionary
print("\nPerson Information:")
print("Hello {name}, you are {age} years old and live in {location}.".format(**person_info))
