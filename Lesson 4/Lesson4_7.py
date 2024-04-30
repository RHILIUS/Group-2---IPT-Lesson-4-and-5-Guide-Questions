# Write a program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

list = [1,1,2,3,4,3,0,0]
list_temp = []
print("List before: ") 
print(list) # [1,1,2,3,4,3,0,0]

for i in list:
  if i not in list_temp:
    list_temp.append(i)

list = list_temp

print("List after: ") 
print(list) # [1, 2, 3, 4, 0]



