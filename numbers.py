#!/usr/bin/python3.6
from random import randint
def random():
    rand_number = randint(0, 100)
    print(rand_number)
    return rand_number
rand_number=random()
answer = 'yes'
while answer == 'yes':
    user_number=int(input('enter your guess number --> '))
    if user_number < rand_number:
        print("Your guess ('{}') lower Than My number ".format(user_number))
    elif user_number > rand_number:
        print("Your guess ('{}')  greater Than My number ".format(user_number))
    else:
        print("Cngrulation You are win".format(user_number))
        while True:
           answer = input("Do you want Play Game agin (Please Enter Yes/No) --> ").lower()
           if answer == 'yes':
               rand_number=random()
               break
           elif answer=='no':
               print("I hope Enjoy it GoodBYE")
               break
           else:
               continue

