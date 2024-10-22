'''So here we are doing a bmi calculator ,'''


print("**Welcome to Bmi calculator**")

#choose your Gender 

print("1.Male\n2.Female")
gender = int(input("enter your choice:"))
if(gender==1):
    print("you choose Male")
elif(gender==2):
    print("you choose Female")
else:
    print('Error , please visit nearest "Mental Hospital"')

Weight = float(input("Enter your weight in Kilograms:"))
Height = float(input("Enter your height in centimeters:"))
Height1= Height*0.01
Age = (input("Enter your Age:"))
#BMI formula = weight / (height)^2
Bmi = (Weight/(Height1*Height1))

if(Bmi<=16):
    print(Bmi,"Severe Thinness")
elif(Bmi>=17 and Bmi<18.5):
    print(Bmi,"Mild Thinness")

elif(Bmi >18.5 and Bmi<=25):
    print(Bmi,"Normal") 
elif(Bmi>=26 and Bmi<=30):
    print(Bmi,"Over weight") 
elif(Bmi>31 and Bmi<=35):
    print(Bmi,"Obese")  
elif(Bmi>=36):
    print(Bmi,"Very Obese ,\nGo Restart Your Life ") 
