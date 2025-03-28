print("welcome to quiz game")

playing=input("do u wnat to play ? (yes/no)").lower()
if(playing!="yes"):
    quit()

def again():
    print("okay,let's play.....")
    score=0

    answer=input("What does CPU stand for? ").lower()
    if(answer=="central processing unit"):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer")

    answer=input("What does GPU stand for? ").lower()
    if(answer=="graphics processing unit"):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer")

    answer=input("What does RAM stand for? ").lower()
    if(answer=="random access memory"):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer")

    answer=input("What does ROM stand for? ").lower()
    if(answer=="read only memory"):
        print("correct answer")
        score=score+1
    else:
        print("incorrect answer")

    print(f"your score is {score} out of 4")
    print(f"you got {score/4*100}%")

#calling the function
again()

#play again loop
while True:
    play_again=input("do u want to play again ? (yes/no)").lower()
    if(play_again!="yes"):
        quit()
    again()