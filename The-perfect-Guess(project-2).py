# the perfect guess 

import random

print("*************  THE PERFECT GUESS  *****************")

list = []  # created empty list and will append all inputted numbers inside it

a = random.randint(1,100)  # generated random number

num = int(input("enter a number : "))  # asked user to guess a no

while(num!=a):  
    if(num<a):
        print("try guessing higher  \U0001F615") 
        num = int(input("enter a number : "))
        list.append(num)  # appends given input in the string
    else:
        if(num>a):
            print("try guessing lower   \U0001F615")
            num = int(input("enter a number "))
            list.append(num)

if num == a:
    print("yay you guessed it right,congrats! \U0001F60E")
    list.append(num)

print("number of guesses it took :  ",len(list))  # len(list) returns no of inputs

print(" ")
print("\U0001F31F  \U0001F31F    \U0001F31F    \U0001F31F     \U0001F31F    \U0001F31F    \U0001F31F    \U0001F31F")



