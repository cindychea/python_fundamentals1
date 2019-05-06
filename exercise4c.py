my_name = "Cindy"
print("What is your name?")
user_name = input()
if my_name.lower() == user_name.lower():
    print("We have the same name!")
else:
    print("Hi {}.".format(user_name))