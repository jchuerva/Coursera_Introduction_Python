# Implementation of classic arcade game Pong
# week 4
# http://www.codeskulptor.org/#user23_QTbEiWTVD6_0.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0, 0]
top= [0, 0]
bottom= [0, 0]
difficulty= 1.10

def ini_paddle():
    global paddle1, paddle2, paddle_vel
    
    #paddle1
    paddle1_center= [HALF_PAD_WIDTH,HEIGHT/2]    
    paddle1_p1= [0, paddle1_center[1]- HALF_PAD_HEIGHT]
    paddle1_p2= [PAD_WIDTH,paddle1_p1[1]]
    paddle1_p3= [0, paddle1_center[1]+ HALF_PAD_HEIGHT]
    paddle1_p4= [PAD_WIDTH,paddle1_p3[1]]
    paddle1= [paddle1_center, paddle1_p1, paddle1_p2, paddle1_p3, paddle1_p4]
    #paddle2
    paddle2_center= [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]    
    paddle2_p1= [WIDTH-PAD_WIDTH, paddle2_center[1]- HALF_PAD_HEIGHT]
    paddle2_p2= [WIDTH,paddle2_p1[1]]
    paddle2_p3= [WIDTH-PAD_WIDTH, paddle2_center[1]+ HALF_PAD_HEIGHT]
    paddle2_p4= [WIDTH,paddle2_p3[1]]
    paddle2= [paddle2_center, paddle2_p1, paddle2_p2, paddle2_p3, paddle2_p4]
    
    #ini_paddle_vel
    paddle_vel= [0, 0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos= [WIDTH/2, HEIGHT/2]
    if direction == 'RIGHT':
        ball_vel[0]= random.randrange(120, 240)/100.0
        ball_vel[1]= 0-random.randrange(60, 180)/100.0
    else:
        ball_vel[0]= 0-random.randrange(120, 240)/100.0
        ball_vel[1]= 0-random.randrange(60, 360)/100.0
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score  # these are ints
    spawn_ball('LEFT')
    ini_paddle()
    score= [0, 0]
    
    
def draw(c):
    global score1, score2, ball_pos, ball_vel, paddle1, paddle2, paddle_vel, top, bottom, score
 
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
        
    # update ball
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    #check if ball touch any pad
    if (ball_pos[1]>= paddle1[0][1]- HALF_PAD_HEIGHT) and (ball_pos[1]<= paddle1[0][1]+ HALF_PAD_HEIGHT):
        touch_left_pad = 1
    else:
        touch_left_pad = 0
        
    if (ball_pos[1]>= paddle2[0][1]- HALF_PAD_HEIGHT) and (ball_pos[1]<= paddle2[0][1]+ HALF_PAD_HEIGHT):
        touch_right_pad = 1
    else:
        touch_right_pad = 0
    
    
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        #left
        if touch_left_pad== 1:
            ball_vel[0]= - ball_vel[0]
            ball_vel[0]= ball_vel[0]*difficulty
        else:
            spawn_ball('RIGHT')
            score[1]+=1
    if ball_pos[0] >= (WIDTH-1)-(BALL_RADIUS+PAD_WIDTH):
        #right
        if touch_right_pad== 1:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0]= ball_vel[0]*difficulty
        else:
            spawn_ball('LEFT')
            score[0]+=1
    if ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:
        #botton
        ball_vel[1] = - ball_vel [1]
    if ball_pos[1] <= BALL_RADIUS:
        #top
        ball_vel[1] = - ball_vel [1]

    
# update paddle's vertical position, keep paddle on the screen
    
    if paddle1[0][1]!= HALF_PAD_HEIGHT and paddle_vel[0]== -1:
        paddle1[0][1]+= paddle_vel[0]
    if paddle1[0][1]!= (HEIGHT- HALF_PAD_HEIGHT) and paddle_vel[0]== 1:
        paddle1[0][1]+= paddle_vel[0]
        
    if paddle2[0][1]!= HALF_PAD_HEIGHT and paddle_vel[1]== -1:
        paddle2[0][1]+= paddle_vel[1]
    if paddle2[0][1]!= (HEIGHT- HALF_PAD_HEIGHT) and paddle_vel[1]== 1:
        paddle2[0][1]+= paddle_vel[1]

    
    paddle1[1]= [0, paddle1[0][1]- HALF_PAD_HEIGHT]
    paddle1[2]= [PAD_WIDTH,paddle1[1][1]]
    paddle1[3]= [0, paddle1[0][1]+ HALF_PAD_HEIGHT]
    paddle1[4]= [PAD_WIDTH,paddle1[3][1]]
    paddle2[1]= [WIDTH-PAD_WIDTH, paddle2[0][1]- HALF_PAD_HEIGHT]
    paddle2[2]= [WIDTH,paddle2[1][1]]
    paddle2[3]= [WIDTH-PAD_WIDTH, paddle2[0][1]+ HALF_PAD_HEIGHT]
    paddle2[4]= [WIDTH,paddle2[3][1]]

    # draw paddles
    c.draw_polygon([paddle1[1], paddle1[2], paddle1[4], paddle1[3]], 2, 'White')
    c.draw_polygon([paddle2[1], paddle2[2], paddle2[4], paddle2[3]], 2, 'White')
   
    # draw scores
    c.draw_text(str(score[0]),(200,100),50,'Green')
    c.draw_text(str(score[1]),(400,100),50,'Green')
    
        
def keydown(key):
    global paddle_vel, paddle1, paddle2
    
    #paddle1 
    if key==simplegui.KEY_MAP["s"]:
        paddle_vel[0]= 1
    elif key==simplegui.KEY_MAP["w"]:
        paddle_vel[0]= -1
    #paddle2
    if key==simplegui.KEY_MAP["down"]:
        paddle_vel[1]= 1
    elif key==simplegui.KEY_MAP["up"]:
        paddle_vel[1]= -1
                  
def keyup(key):
    global paddle_vel
    
    if key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
        paddle_vel[1]= 0
    
    if key==simplegui.KEY_MAP["s"] or key==simplegui.KEY_MAP["w"]:
        paddle_vel[0]= 0

#reset button        
def reset_button():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#define button
frame.add_button('Reset Game', reset_button)

# start frame
new_game()
frame.start()
