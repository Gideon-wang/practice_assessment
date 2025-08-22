'''
      author:Gideon Wang
      version:1
      date:21/08/2025
      description:guessing game
'''
#------------------libraries-----------------
import random#to get a random number by using random.randint
import string#get the ascii alphabet
#------------------functions-----------------
#--------------------------
#This function creates a list and use random number to choose one of them 
#and then compare the user input with the correct answer
#to check who wins the round
#--------------------------
def heads_tails():
    user_score=0
    computer_score=0
    options=["Heads","Tails"]#creating a list including the two options
    while user_score!=2 and computer_score!=2:#winning/losing conditions
        choice=random.randint(0,1)#random number
        computer_guess=options[choice]#random choice
        user_guess=str(input("Heads or Tails"))        
        #this loop is to make sure the user's input is valid for the computer to compare with the correct answer
        if user_guess.isalpha():
            if user_guess=="Heads" or user_guess=="Tails":
                #this loop is to check whether or not the answer is right
                if user_guess==computer_guess:
                    print("it was{},you guessed{},you won that round".format(computer_guess,user_guess))
                    user_score+=1
                else:
                    print("it was{},you guessed{},you lost that round".format(computer_guess,user_guess))
                    computer_score+=1
            else:
                print("the word you entered is incorrect")#exclude words that do not meet the requirements
        else:
            print("please enter the word")#exclude number,blank and such invalid input

    #the loops has now ended and it will output won the beat of 3 rounds
    if user_score==2:
        print(f"{first_name},you won that game")
    else:
        print(f"{first_name},you lost that game")

#--------------------main program--------------------------
print("hi!welcome to my heads ot tails game")#greetings
#this loop is making sure the name user entered is valid
while True:#keep on looping while the user enter valid name
    first_name=(input("what is your name"))#record the name in string
    if len(first_name)>=2 and len(first_name)<=13:
        if first_name.isalpha(): #to make sure there is no any blank in the name
            break
        else:
            print("the name you entered is invalid")
    else:
        print("invalid name length")#exclude invalid name length
while True:#keep on looping while. the user enter valid age
    try:
        age=int(input("what is your age"))#record the age in number
        if age>=1 and age<=130:
            break
        else:
            print("your age must in range 1-130")#exclude invalid age number
    except:
        print("the age you entered is invalid")#exclude words,blank and such invalid input for age
heads_tails()#this calls up the function