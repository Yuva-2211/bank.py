
#rock , paper , scissors  game 

import random
'''**rules**
rock vs paper  = paper wins
rock vs scissors = rock wins
paper vs scissors = scissors wins 

'''

computer = random.choice([-1,0,1])#-1,0,1 refers to rock , paper , scissors
youx= input("enter your choice:")
youDict = {'r':-1 , 'p':0 ,'s':1}
reverseDict={-1:'Rock',0:"Paper",1:"Scissors"}

you = youDict[youx]

print(f"you chose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer==you):#the first condition
    print("its a Draw ")


else:   #nested conditions wrt else
    if(computer==-1 and you==0):
     print("you win!!")
    elif(computer==-1 and you==1):
     print('you loose , better luck next time') 
    elif(computer==0 and you==1):
     print('you win!!')
    elif(computer==0 and you==-1):
     print("you loose , better luck next time ")    
    elif(computer==1 and you==-1):
     print("you win!!")
    elif(computer==1 and you==0):
     print('you loose , better luck next time')
    else:
      print('1ERROR 404@#@')
