#Age calculator 

from datetime import datetime

print('Welcome to Age Calculator')
def age_cal(dob):
    today = datetime.today()
    age = age = today.year - dob.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
        
    return age
age = input("enter your dob,in YYYY/MM/DD : ")
birthdate = datetime.strptime(age, "%Y/%m/%d")

final = age_cal(birthdate)
print(f"Your age is{final}")


"""Error i faced building logic initially
1) age = datetime.today() - datetime.year , It should be age = today.year - dob.year.
2)Misconceptions on Date time mod but through Documentation , cleared it"""