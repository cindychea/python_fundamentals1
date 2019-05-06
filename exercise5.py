# Create initial while loop
# Add go home (added as quit)
# Keep track of energy
# Let user rest and eat
distance_from_home = 0
energy = 50
print("You're starting your workout from home. Your energy level is 50.")
while True:
    print("Would you like to walk, run, sprint, break, eat, or quit?")
    travel_mode = input()
    if travel_mode == "run" or travel_mode == "r" or travel_mode == "sprint" or travel_mode == "s" and energy <= 0:
        print("You do not have enough energy to run or sprint right now!")
        continue
    if energy >= 100:
        print("I think it's time to work a little harder!")
    if distance_from_home >= 100:
        print("Great job, but you're awfully far from home! Consider calling it a day.")
    if travel_mode == "walk" or travel_mode == "w":
        distance_from_home += 1
        energy += 3
    elif travel_mode == "run" or travel_mode == "r":
        distance_from_home += 5
        energy -= 5
    elif travel_mode == "sprint" or travel_mode == "s":
        distance_from_home += 10
        energy -= 10
    elif travel_mode == "break" or travel_mode == "b":
        energy += 5
    elif travel_mode == "eat" or travel_mode == "e":
        energy += 10
    elif travel_mode == "quit" or travel_mode == "q":
        print("You've finished your workout! Goodbye!")
        break
    else:
        print("Invalid answer. Please choose walk, run, sprint, break, eat, or quit.")
    print("Distance from home is {} km.".format(distance_from_home))
    print("Your energy level is {}.".format(energy))