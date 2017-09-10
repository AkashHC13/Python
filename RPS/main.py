#!/bin/python3
from random import randint

player = raw_input('rock (r), paper (p) or scissors (s) ?')
print(player)

chosen = randint(1,3)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print player + " vs " + computer

if player == computer:
    print "OOPS! its a draw"
elif player == 'r' and computer == 'p':
    print "Player wins!"
elif player == 'r' and computer == 's':
    print "Player wins!"
elif player == 'p' and computer == 'r':
    print "computer wins"
elif player == 'p' and computer == 's':
    print "computer wins"
elif player == 's' and computer == 'r':
    print "computer wins"
else:
    print "Player wins"
