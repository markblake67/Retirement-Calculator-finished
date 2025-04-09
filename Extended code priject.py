name = input("Enter name: ")
age = input("Enter Age: ")
try:
    age = int(age)
except:
    ValueError
    age = input("Please Enter an Integer: ")
    
def retirementCalc(x):
    yearsToRetire = 66 - int(age)
    if yearsToRetire > 0:
        yearsToRetire = str(yearsToRetire)
        print(f"You have: {yearsToRetire} years until you can retire.")
    else:
        print("You can retire!")
    
print(f"Hello, {name}.")
retirementCalc(age)