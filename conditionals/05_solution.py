weather = str(input("Enter weather: "))
# print(type(weather))
weather = weather.lower()


if weather == "sunny":
    activity ="Go for a walk"
elif weather == "rainy":
    activity ="Stay home and read a book"
elif weather == "snowy":
    activity ="Cover your self up and go out make snowman"

print(activity)