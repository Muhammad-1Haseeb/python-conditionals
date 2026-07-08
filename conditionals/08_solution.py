password = str(input("Enter your password: "))

if len(password)<6:
    strength = "weak"
elif len(password)>= 6 and len(password)<10:
    strength = "medium"
elif len(password)>= 10 and len(password)<15:
    strength = "strong"
else:
    strength = "very long"

print("Password strength: ",len(password))