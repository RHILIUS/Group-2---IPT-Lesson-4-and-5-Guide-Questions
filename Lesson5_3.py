# GUIDE QUESTION 3

days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

# INPUT 
month = input("Enter a month (atleast 3 letters): ")

#USING SLICING METHOD TO ACCEPT  ATLEAST 3 LETTERS IN THE INPUT
keyMatched= [key for key in days.keys() if key[:3].lower() == month[:3].lower()]


if keyMatched:
    for key in keyMatched:
        print(f"{key}: {days[key]} days")
else:
    print("Invalid input.")


# SORTED MONTHS
print("\nSORTED MONTHS: ")
for i in sorted(days.keys()):
    print(i)
    
# MONTHS WITH 31 DAYS IN IT
print("\nMONTHS WITH 31 DAYS: ")
for i in days:
    if days[i] == 31:
        print(i)

# SORTED DICTIONARY BASED ON NO. OF DAYS IN IT
print("\nSORTED BASED ON DAYS: ")
for i, j in sorted(days.items(), key=lambda x:x[1]):
    print(f"{i}: {j}")
