# implementation of card game - Memory
# week 5
# http://www.codeskulptor.org/#user24_SwalRJ0BWQ_4.py

import simplegui
import random

LENGHT_FRAME= 800
WIDTH_FRAME= 100

# define de lists
list_numbers= list( range(8)) + list( range(8))
exposed= [False] * len(list_numbers)
inside_celd= list(exposed)
LENGHT_CELD= LENGHT_FRAME/len(list_numbers) 


# helper function to initialize globals
def new_game():
    global exposed, inside_celd, cards_exposed, turn, prev_position, end_game, position
    random.shuffle(list_numbers)
    exposed= [False] * len(list_numbers)
    inside_celd= list(exposed)
    cards_exposed= 0
    turn= 0
    label.set_text("Turns = "+ str(turn))
    prev_position= -1
    end_game= False
    position=-1
    
        
     
# define event handlers
def mouseclick(pos):
    global inside_celd, cards_exposed, turn, exposed, prev_position, list_numbers, end_game, position
    #check the card clicked by the mouse
#    print str(turn)
    #detect where is the mouse
    for line in range(len( list_numbers)):
        if pos[0] >= (LENGHT_CELD * line) and pos[0]<= (LENGHT_CELD * (line+1)):
            if exposed[ line]== False:
                position= int(line)
            #pos= value of celd with the mouse
    if position!= prev_position and end_game== False and inside_celd[ position]== False:
        if cards_exposed== 0:
            #0 cards exponed
            cards_exposed= 1
            inside_celd[ position]= True
        elif cards_exposed== 1:
            #1 card exponed
            cards_exposed= 2
            turn+= 1
            label.set_text("Turns = "+ str(turn))
            inside_celd[ position]= True
            #check if cards are the same
            if list_numbers[ position]== list_numbers[ prev_position]:
                #print "Iguales!!"
                exposed[ position]= True
                exposed[ prev_position]= True
        elif cards_exposed== 2:
            cards_exposed=1
            inside_celd= [ False] * len( list_numbers)
            inside_celd[ position]= True
    prev_position= int(position)
    if exposed == [True] * len(list_numbers):
        print "Game finshed in "+ str(turn)+ " turns!!"
        end_game= True

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #global variables
    global exposed, inside_celd, turn
    #draw lines of separation
    for line in range(len(list_numbers)):
        #draw the lines
        if line !=0:
            canvas.draw_line((LENGHT_CELD * line, 0), (LENGHT_CELD * line, WIDTH_FRAME), 2, "Grey")
        #draw the numbers in each celd if exposed is true
        if inside_celd[ line] or exposed[ line]:
            #draw background of the celd
            tl= [(LENGHT_CELD * line) +1, 0]
            bt= [tl[0],WIDTH_FRAME]
            tr= [(LENGHT_CELD * (line+1)) -1, 0]
            br= [tr[0], WIDTH_FRAME]
            if exposed[ line]:
                #blue when the match has been found
                canvas.draw_polygon([tl, bt, br, tr], 1, "Blue", "Blue")
            else:
                #not found = color green
                canvas.draw_polygon([tl, bt, br, tr], 1, "Green", "Green")
            #draw text
            canvas.draw_text(str(list_numbers[ line]), ((LENGHT_CELD * line)+ (1.0/3)* LENGHT_CELD, 2.0* WIDTH_FRAME/3), 35, 'White')
    if end_game:
        canvas.draw_text("Game finshed in "+ str(turn)+ " turns!!", (4.5*LENGHT_CELD,WIDTH_FRAME/2), 35, 'Red')
                

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", LENGHT_FRAME, WIDTH_FRAME)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric