# Create initial while loop
# Add go home (added as quit)
distance_from_home = 0
while True:
    print("Would you like to walk or run?")
    travel_mode = input()
    if travel_mode == "walk" or travel_mode == "w":
        distance_from_home +=1
    elif travel_mode == "run" or travel_mode == "r":
        distance_from_home += 5
    elif travel_mode == "quit" or travel_mode == "q":
        print("Great job! Goodbye!")
        break
    else:
        print("Invalid answer. Please choose walk, run, or quit.")
    print("Distance from home is {} km.".format(distance_from_home))