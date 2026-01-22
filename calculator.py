num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("select operation")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
option = input("Enter option (1/2/3/4): ")
if option == "1":
    print("Result:", num1 + num2)
elif option == "2":
    print("Result:", num1 - num2)
elif option == "3":
    print("Result:", num1 * num2)
elif option == "4":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid option")

