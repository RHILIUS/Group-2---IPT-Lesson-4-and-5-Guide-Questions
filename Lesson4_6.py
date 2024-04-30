# Write a program that asks the user for an integer and creates a list that consists of the factors of that integer


num = int(input("Enter a number: "))

factors = []
for i in range(1, num + 1): 
  if num % i == 0:
    factors.append(i)

print(f"Factors of {num}: {factors}")