import random

top_range=input("Enter top range:")
print()

if top_range.isdigit():
        top_range=int(top_range)

random_number= random.randint(0,top_range)
print("Start ur Guessing......")
print()
attempt=5
print(random_number)
count=0

while attempt>=1:
    print()
    print(f"You have {attempt} attempt to guess the number")
    user_guess=input(f"Make a guess between 0 to {top_range}: ")

    if user_guess.isdigit():
        user_guess=int(user_guess)

        if(user_guess==random_number):
            print()
            print(f"you got it after {count} attempt")
            break
        else:
            print("oops u failed!")
            count=count+1
    attempt=attempt-1

    

"""         if(user_guess>top_range):
                print("Your guess number is above the Top range")
                count=count+1
            elif(user_guess<top_range):
                print("Your guess number is below the Top range")
                count=count+1
            else:
                print("oops u failed!")
                count=count+1
"""