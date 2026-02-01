print("-----Basic Calculator-----")

while True:
    print("Which Option you want to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice"))

    if choice == 5:
        print("Exiting Calculator...")
        break

    x = float(input("Enter the num1: "))
    y = float(input("Enter the num2: "))
    
    if choice == 1:
        sum = x + y
        print(f"Sum is: {sum}")
    elif choice == 2:
        diff = abs(x - y)
        print(f"Diff is: {diff}")
    elif choice == 3:
        prod = x * y
        print(f"Product is: {prod}")
    elif choice == 4:
        if y == 0:
            print("0 cannot be divided")
        else:
            division = x / y
            print(f"division is: {division}")
    else:
        print("invalid Choice")