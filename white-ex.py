import random
lives = 3
while lives > 0:
    print("You have", lives, "lives left.")
    dice = random.randint(1,6)
    print("Your rolled a", dice)
    if dice == 6:
        print("\n\nYOU WIN!\n\n")
        break
    else:
        lives = lives -1

else:
    print("\n\nYOU LOSE!\n\n")

print("Thank you for playing. Goodbye.")
