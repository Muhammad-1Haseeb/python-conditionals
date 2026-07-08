# pet food recommendation based on pet type and age
pet_type = "Dog"
age = 5
if pet_type == "Dog":
    if age < 1:
        food = "Puppy Food"
    elif age >= 1 and age < 7:
        food = "Adult Dog Food"
    else:
        food = "Senior Dog Food"
elif pet_type == "Cat":
    if age < 1:
        food = "Kitten Food"
    elif age >= 1 and age < 10:
        food = "Adult Cat Food"
    else:
        food = "Senior Cat Food"
else:
    food = "Unknown pet type"
print("Recommended food for your pet: ", food)

