# Start with the list [8,9,10]. Do the following: 
list = [8,9,10]
print("List before: ")
print(list)


# a. Set the second entry (index 1) to 17
list[1] = 17 # [8, 17, 10]

# b. Add 4, 5, and 6 to the end of the list 
list.extend([4,5,6]) # [8, 17, 10, 4, 5, 6]

# c. Remove the first entry from the list 
list.pop(0) # [17, 10, 4, 5, 6]

# d. Sort the list 
list.sort() # [4, 5, 6, 10, 17]

# e. Double the list f. Insert 25 at index 3 
list = list + list # [4, 5, 6, 10, 17, 4, 5, 6, 10, 17]
list.insert(3,25) # [4, 5, 6, 25, 10, 17, 4, 5, 6, 10, 17]


# The final list should equal [4,5,6,25,10,17,4,5,6,10,17] 

print("List after: ")
print(list)  # [4, 5, 6, 25, 9, 10, 17, 4, 5, 6, 9, 10, 17]


