print("Please enter your age.")
user_age = input()
years_apart = 25 - int(user_age)
if int(user_age) <= 105:
    print("We are {} years apart.".format(abs(years_apart)))
else:
    print("I'm not sure I believe you.")