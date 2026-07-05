age = input("Enter your age: ")

age_in_int = int(age)
if age_in_int <= 13:
        print("You are a child")

if age_in_int >= 13 and age_in_int < 19:
        print("You are a teenager")

if age_in_int >= 19 and age_in_int < 60:
        print("You are an adult")
if age_in_int >= 60:
        print("You are a senior citizen")

