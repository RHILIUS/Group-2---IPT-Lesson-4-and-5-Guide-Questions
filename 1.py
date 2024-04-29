list_of_tup = []

# Prompt for values
number_of_tuples = int(input("How many tuples do you want to create: "))
print("=========================")

for i in range(1,number_of_tuples + 1):
    print(f"Tuple no: {i}")
    num = int(input("Enter number: "))
    square = num * num

    tup = (num,square)
    list_of_tup.append(tup)

    print("=========================")

print(f"List of tuple: {list_of_tup}")
