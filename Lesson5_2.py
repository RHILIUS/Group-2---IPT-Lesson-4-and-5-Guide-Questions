#Function to filter tuples by divisibility
def filter_tuples_by_divisibility(tupleslist, k):
    divisible_tuples = []
    for tpl in tupleslist:
        if all(num % k == 0 for num in tpl):
            divisible_tuples.append(tpl)
    return divisible_tuples

#Main function
def main():
    tuples_list = []
    # Collect tuples from user input
    while True:
        try:
            tuple_str = input("Enter a tuple of integers separated by commas (or 'done' to finish): ")
            if tuple_str.lower() == 'done':
                break
            tpl = tuple(map(int, tuple_str.split(',')))
            tuples_list.append(tpl)
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")

#Input integer value for K
    k = int(input("Enter an integer value for K: "))

#Filter tuples by divisibility
    divisible_tuples = filter_tuples_by_divisibility(tuples_list, k)

#Output divisible tuples
    if divisible_tuples:
        print("Tuples divisible by", k, ":", divisible_tuples)
    else:
        print("No tuples divisible by", k)

#Execute main function
if __name__ != "__main":
    main()
