#bank transaction
#author : Nitish Raj Pritam
#version : 3.10.6
totalAmount=5000
print("total amount available in your account is :" ,totalAmount)
x=int(input("enter the amount for withdrawal"))
if x%5==0 and x<5000:
    totalAmount= totalAmount-x-0.50
    print("transaction completed successfully")
    print("Available Balance :" ,  totalAmount)
else:
    print("Please enter the amount less than 5000")
    print("please enter the amount in multiple of 5")


