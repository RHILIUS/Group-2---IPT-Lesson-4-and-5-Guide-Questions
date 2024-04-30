# Write a program that asks the user to enter size of list and input a list of integers. Do the following:

size = int(input("Enter size: "))
list = [] 
for i in range(size):
  num = int(input(f"Value #{i+1}: "))
  list.append(num)

print("\nOriginal List: ")
print(list)
print("===============================")

# a. Print the sum of items in the list.
sum_of_items = sum(list)
print(f"Sum of items: {sum_of_items}")

# b. Print the last item in the list. 
last_item = list[-1]
print(f"Last item: {last_item}")

# c. Print the list in reverse order.
reverse_order = list[::-1]
print(f"List in reverse order: {reverse_order}")

# d. Print Yes if the list contains a 5 and No otherwise. 
if 5 in list:
  print("List contains 5: Yes")
else:
  print("List contains 5: No")

# e. Print how many integers in the list are less than 5. 
count = 0 
for i in list:
  if i < 5:
    count = count + 1
print(f"Integers less than 5: {count}")

# f. Remove the first and last items from the list, sort the remaining items, and print the result.
list.pop(0)
list.pop(-1)

list.sort()
print("===============================")

print("List After: ")
print(list)
