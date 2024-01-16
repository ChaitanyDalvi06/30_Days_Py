#Day 2: Basic Arithmetic: Write a program to perform basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers entered by the user.

num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
opr=(input("Enter the operation + , - , * , /  :  "))
if opr=='+':
    print('Addition of both numbers are : ',num1+num2)
if opr=='-':
    print('substraction of both numbers are : ',num1-num2)
if opr=='*':
    print('multiplicaton of both numbers are : ',num1*num2)
if opr=='/':
    print('divide of both numbers are : ',num1/num2)  
              