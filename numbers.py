#!/usr/bin/python3.6
from random import randint
def random():
    rand_number = randint(0, 100)
    return rand_number
rand_number=random()
guess_attempt=0
answer = 'yes'
while answer == 'yes':
    user_number=int(input('enter your guess number --> '))
    guess_attempt+=1 #this variables for attempt count
    if user_number < rand_number:
        print("Your guess ('{}') lower Than My number.Enter a larger Numeber --> ".format(user_number))
    elif user_number > rand_number:
        print("Your guess ('{}')  greater Than My number.Enter a lower number --> ".format(user_number))
    else:
        print("congratulations :). You are win You guessed your {} attempt.".format(guess_attempt))
        guess_attempt=0
        while True:
           answer = input("Do you want Play Game agin (Please just Enter Yes/No) --> ").lower()
           if answer == 'yes':
               rand_number=random()
               break
           elif answer=='no':
               print("I hope Enjoy it GoodBYE")
               break
           else:
               continue
