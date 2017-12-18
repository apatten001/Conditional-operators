
# you can combine conditions with logical operators and or not


name = input("What is your name?: ")
body_fat = int(input("What is your body fat percentage?: "))

if (body_fat >= 25) and (body_fat < 30):
    print(" {} you are overweight".format(name))
elif body_fat >= 30:
    print(" {} you are considered obese".format(name))
elif (body_fat <= 6) or (body_fat < 2):
    print("{} ,you are underweight".format(name))

else:
    print("{} you are within the normal body fat range ".format(name))