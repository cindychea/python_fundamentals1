secret_number = 3
print("Please enter a number.")
user_number = input()
if int(user_number) == secret_number:
    print("You win!")
elif abs(int(user_number)-secret_number)==1:
    print("So close!")
else:
    print("Try again.")