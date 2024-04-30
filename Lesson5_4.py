product = {}

# Enter product names and prices into the dictionary
while True:
    x = True
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    #key - value insertion
    if product_name in product:
        print(f"product already listed, would you like to overwrite [{product_name}]?")
        choice = input("(y if yes | Any if no):")
        if choice.lower() == "y":
            product[product_name] = price
        else:
            x = False
            
        
    if x is True:
        product[product_name] = price

    print("=========================")
    
    choice = input("Do you want to add a product again? (y if yes | Any if no): ")

    if choice.lower() != "y":
        break
print("list of products: ")
for x in product:
    print(f"{x}\t\t\t{product[x]}")
    pass

# Search for a product
is_searching = True
print("=========================")

print("Search for a product: ")
while is_searching == True:
    product_to_search = input("Enter the product name to search: ")
    product_found = False
    for product_name in product:
        if product_name.lower() == product_to_search.lower():
            print(f"Product name: {product_name}")
            print(f"Price: {product[product_name]}")
            product_found = True
            print("=========================")
        

    if product_found == False:
        print("Product is not found")
        print("=========================")
        

    choice = input("Do you want to search again? (y if yes | Any if no): ")

    if choice.lower() != "y":
        print("Goodbye")
        is_searching = False
        print("=========================")
   


