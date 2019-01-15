#!/usr/bin/python3.6
from random import randint
def geme_level():
    try:
        print("Choise Game Level  >>>\n 1.EASY \n 2.NORMAL \n 3.HARD")
        answer=int(input(">>> "))
    except:
        geme_level()
    if answer == 1:
        return 10
    elif answer == 2:
        return 7
    else:
        return 5    
def random():
    rand_number = randint(0, 100)
    return rand_number
rand_number=random()
guess_attempt=0
answer = 'yes'
score=100
level=int(geme_level())
print("Your Lif {}/{}".format(level - guess_attempt, level))
while answer == 'yes':
    while True:
        try:
            user_number=eval(input('enter your guess number >>> '))
            break
        except:
            print("Please enter Number for this Game Try")
            continue
    guess_attempt+=1 #this variables for attempt count
    if (user_number < rand_number) & (guess_attempt < level):
        print("Your guess ('{}') lower Than My number.Enter a larger Numeber --> ".format(user_number))
        print("Your Lif {}/{}".format(level-guess_attempt,level))
        print("Your score is {}".format(score))
        score-=10
    elif (user_number > rand_number) & (guess_attempt < level):
        print("Your guess ('{}')  greater Than My number.Enter a lower number --> ".format(user_number))
        print("Your Lif {}/{}".format(level - guess_attempt, level))
        print("Your score is {}".format(score))
        score-=10
    else:
        if guess_attempt == level:
            print("You are Lose  :(. Dont Wory. Try agin.You Win next Try".format(guess_attempt))
            print('You Score is 0')
        else:
            print("congratulations :). You are win You guessed your {} attempt.".format(guess_attempt))
            score+=50
            print("Your score is {}".format(score))
            guess_attempt=0
        while True:
           answer = input("Do you want Play Game agin (Please just Enter Yes/No) --> ").lower()
           if answer == 'yes':
               score=100
               rand_number=random()
               break
           elif answer=='no':
               print("I hope Enjoy it GoodBYE")
               break
           else:
               continue
