# Starting with the list of the previous exercise, write Python statements to do the following: 
list = [67, 62.9, 'hi', False, 8, 67, 'apple', 6.5]

print("List before: ")
print(list) # [67, 62.9, 'hi', False, 8, 67, 'apple', 6.5]
print("===================================================")

# a. Append “banana” and 67 to the list. 
list.append("banana") # [67, 62.9, 'hi', False, 8, 67, 'apple', 6.5, 'banana']
list.append(67) # [67, 62.9, 'hi', False, 8, 67, 'apple', 6.5, 'banana', 67]

# b. Insert the value “dog” at position 3. 
list.insert(3, "dog") # [67, 62.9, 'hi', 'dog', False, 8, 67, 'apple', 6.5, 'banana', 67]

# c. Insert the value 909 at the start of the list. 
list.insert(0, 909) # [909, 67, 62.9, 'hi', 'dog', False, 8, 67, 'apple', 6.5, 'banana', 67]

# # d. Find the index of “hi”. 
index_of_hi = list.index("hi")
print(f"hi is at index {index_of_hi}") # hi is at index 3

# e. Count the number of 67s in the list. 
count = list.count(67) 
print(f"The number of 67s in the list is {count}") # The number of 67s in the list is 3

# f. Remove the first occurrence of 67 from the list. 
list.remove(67) # [909, 62.9, 'hi', 'dog', False, 8, 67, 'apple', 6.5, 'banana', 67]

# # g. Remove False from the list using pop and index
index_false = list.index(False)
list.pop(index_false) # [909, 62.9, 'hi', 'dog', 8, 67, 'apple', 6.5, 'banana', 67]


print("===================================================")
print("List after: ") 
print(list) # [909, 62.9, 'hi', 'dog', 8, 67, 'apple', 6.5, 'banana', 67]
