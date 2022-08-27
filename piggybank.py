#Total amount calculation for Piggybank
#author : Nitish Raj Pritam
#version : 3.10.6
coin1=input("enter the number of coin of rs 1")
if(coin1.isdigit()):
    coin1=int(coin1)
else:
    print("Invalid Input!!")
    exit()
coin2=input("enter the number of coin of rs 2")
if(coin2.isdigit()):
    coin2=int(coin2)
else:
    print("Invalid Input!!")
    exit()
coin5=input("enter the number of coin of rs 5")
if(coin5.isdigit()):
    coin5=int(coin5)
else:
    print("Invalid Input!!")
    exit()
coin10=input("enter the number of coin of rs 10")
if(coin10.isdigit()):
    coin10=int(coin10)
else:
    print("Invalid Input!!")
    exit()
total=coin1*1+coin2*2+coin5*5+coin10*10
print("total amount :" , total) 
