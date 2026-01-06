num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
print("select the Operation of your choice:")
print("1.Addition(+)")
print("2.Subtraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
choice=input("choose any arithmetic operation from above (1/2/3/4)")
if choice=="1":
    result=num1+num2
    print("Result:",result)
elif choice=="2":
    result=num1-num2
    print("Result:",result)
elif choice=="3":
    result=num1*num2
    print("Result:",result)
elif choice=="4":
    if num2!=0:
     result=num1/num2
     print("Result:",result)
    else:
        print("Error. Division is not allowed by zero")
else:
    print("Invalid choice. please select a valid operation")