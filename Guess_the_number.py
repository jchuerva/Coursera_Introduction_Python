# "Guess the number" mini-project
# week 2
# http://www.codeskulptor.org/#user21_IOsPdqZjLJ_5.py

# Description:
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import libraries
import random
import simplegui
import math


# initialize global variables used in your code
low = 0

def calculate_guesses(low,high):
# funtion to calculate the number of guesses
    return math.ceil(math.log( high- low+ 1, 2))

def new_game():
# helper function to start and restart the game 
    global guesses,high,low,guess_num
    guesses = int(calculate_guesses( low,high))
    guess_num= random.randrange( low, high)
    print "##############################"
    print "Your game has been initialized"
    print "##############################"
    print "The guess number range is [",low,", ",high,")"
    print "Number of guesses:", guesses

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts the game
    global high
    high = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts the game
    global high
    high = 1000
    new_game()

    
def input_guess(guess):
    # fution that check the number of guesses and if the guess number is right
    global guesses,guess_num
    if guesses <= 1:
        print "#########"
        print "You loose"
        print "#########"
        print "Guess number not found. Guess number:",guess_num
        new_game()
    elif int(guess) == guess_num:
        print "########"
        print "You win!"
        print "########"
        print "Guess number found. Guess number:", guess_num
        new_game()
    elif int(guess) < guess_num:
        guesses-=1
        print "The guess number is: Higher"
        print "Number of guesses:", guesses
        print "----"
    else:
        guesses-=1
        print "The guess number is: Lower"
        print "Number of guesses:", guesses
        print "----"

   
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button("restart", new_game)
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_input("Enter the guess number", input_guess, 200)


# call new_game and start frame
range100()


# always remember to check your completed program against the grading rubric
