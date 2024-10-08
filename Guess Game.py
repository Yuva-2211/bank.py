''''this a guess game  where we have to guess a number between 1 to 20'''

import random
computer = random.randint(0,10)
a = int(input("enter your guess:"))
while (computer!=a):
    if(a>computer):
        print("lower number please!!")
        a = int(input("enter your guess:"))
    elif(a<computer):
        print("higher number please!")
        a = int(input("enter your guess:"))
else:
      print('Yup you guessed it Right!! this is',a,"the secret number you you guessed!! ")    




    
    