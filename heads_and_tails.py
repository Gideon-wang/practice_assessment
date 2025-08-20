'''
      author:Gideon Wang
      version:1
      date:21/08/2025
      description:guessing game
'''
import random
def heads_tails():
    user_score=0
    computer_score=0
    options=["Heads","Tails"]
    while user_score!=2 and computer_score!=2:
        choice=random.randint(0,1)
        computer_guess=options(choice)
        user_guess=str(input("heads or tails"))
        if user_guess==computer_guess:
            print("it was{},you guessed{},you won that round".format(computer_guess,user_guess))
            user_score+=1
        else:
            print("it was{},you guessed{},you lost that round".format(computer_guess,user_guess))
            computer_score+=1
#the loops has now ended and it will output won the beat of 3 rounds
    if user_score==2:
        print("{},you won that game".format(first_name))
    else:
        print("{},you lost that game".format(first_name))

#main program
print("hi!welcome to my heads ot tails game")
first_name=str(input("what is your name"))
age=int(input("what is your age"))
heads_tails()#this calls up the function