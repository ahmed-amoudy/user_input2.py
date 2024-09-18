#Write a program that accepts user input to create two sets of integers.
#Then, create a new set that contains only the elements that are common to both sets.
# Program to find common elements in two sets of integers

# Function to create a set of integers from user input
def create_set(set_num):
    print(f"Enter integers for Set {set_num}, separated by spaces:")
    user_input = input()
    return set(map(int, user_input.split()))  # Convert the input string to a set of integers

# Create two sets
set1 = create_set(1)
set2 = create_set(2)

# Find common elements using intersection
common_elements = set1 & set2  # Alternatively, you can use set1.intersection(set2)

# Display the result
print("\nCommon elements between the two sets:")
print(common_elements)
