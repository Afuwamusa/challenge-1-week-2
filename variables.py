#a programme covering input/out put/variables and conditional logic
year_of_birth =input("enter year of birth: ")
year = int(year_of_birth)
age = 2019 - year
if age < 18:
    print("this person is a minor")
elif age >= 18 and age <= 36:
    print("the person is a youth")
else:
    print("the person is an elder")


