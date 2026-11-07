import random
top_of_range = input("enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please enter a number next time")
        quit()
else:
     print("please enter a number next time")
     quit()
random_number= random.randint(0,top_of_range)
guesses = 0
while True:
    guesses+=1
    try:
        user_guess = int(input("enter a number: "))
    except ValueError:
        print("enter a valid number")
        continue
    if user_guess == random_number:
        print("you got it right")
        break
    elif user_guess > random_number:
        print("you are above the number")
    else:
        print("you are below the number")
print("you got it", guesses, "guesses")

