# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random


def number_to_name(number):
    #transform from numbers into names
    if number==0:
        return 'rock'
    elif number==1:
        return 'Spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    else:
        print "Wrong number"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!


def name_to_number(name):
    #transform names into numbers
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        print "Wrong name"

def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    differenc = player_number - comp_number
    # use if/elif/else to determine winner
    res = differenc % 5
    if (res == 1 or res == 2):
        winner= "Player wins!\n"
    elif (res == 3 or res == 4):
        winner= "Computer wins!\n"
    else:
        winner= "Player and computer tie!\n"
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    # print results
    print "Player chooses",name
    print "Computer chooses",comp_name
    print winner
    
    return 0
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


