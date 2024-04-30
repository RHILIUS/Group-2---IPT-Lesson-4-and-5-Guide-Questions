# Define the variables x and y as lists of numbers 
x = [1,2,3,4,5]
y = [11,12,13,14,15]
z = (21,22,23,24,25)

# a. What is the value of 3*x? 
print(3*x)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# b. What is the value of x+y?
print(x+y) # [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]

# c. What is the value of x-y? 
# Error! '-' is not applicable for lists

# d. What is the value of x[1]? 
print(x[1]) # 2

# e. What is the value of x[0]?
print(x[0]) # 1

# f. What is the value of x[-1]? 
print(x[-1]) # 5

# g. What is the value of x[:]?
print(x[:]) # [1, 2, 3, 4, 5] Displays all elements in the list

# h. What is the value of x[2:4]? 
print(x[2:4]) # [3, 4]

# i. What is the value of x[1:4:2]? 
print(x[1:4:2]) # [2, 4]

# j. What is the value of x[:2]? 
print(x[:2]) # [1, 2]

# k. What is the value of x[::2]?
print(x[::2]) # [1, 3, 5]

# l. What is the result of the following two expressions? 
# x[3]=8 
# print x
x[3]=8
print(x) # [1, 2, 3, 8, 5]


 
