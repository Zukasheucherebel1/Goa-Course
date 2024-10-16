name=input("whats your name:")
print(name)
lastname=input("whats your lastname:")
print(lastname)
gmail=input("what is your gmail:")
print(gmail)
age=int(input("whats your age:"))
print(age)


num1=input("chose number")

num2=input("chose number")
           
print("num1"+"num2")

#input არის ინფორმაცია რომელიც კომპიუტერში შედის
#output არის ინფორმაცია რომელიც კომპიუტერიდან გამოდის


num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))

operation=input("enter an operation ( +, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1*num2) 
elif operation == "/":
    print(num1 / num2) 

else:
     print("invaild operation!")

