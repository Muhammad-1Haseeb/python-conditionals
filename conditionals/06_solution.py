distance = 5

if distance < 3:
    transport = "Walk"
elif distance >= 3 and distance < 15:
    transport = "Bike"
else:
    transport = "Drive"

print(transport)