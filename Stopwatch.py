# "Stopwatch: The Game"
# week 3
# http://www.codeskulptor.org/#user22_RNXwCY7Ymq_0.py

import simplegui
# define global variables
global tenthsec, num_stop, num_win, D, stop
tenthsec = 0
num_stop=0
num_win=0
stop=True


# define helper function format that converts time
def format(t):
#format timer to A:BC.D, A=min, BC=second and D=tenths of seconds
    global tenthsec,D,stop
    A='0'
    BC='00'
    D='0'
    if t>0:
        D=str(t)[len(str(t))-1:]
        if t > 10:
            BC=str(t)[:len(str(t))-1]
            if int(BC)>60:
                A=str(int(BC)/60)
                BC=str(int(BC)%60)
            if len(BC)==1:
                BC='0'+BC
            if ((int(A) == 9) and (int(BC)==99) and (int(D)==9)):
                tenthsec = 0
                timer.stop()
    return A+ ':'+ BC+ '.'+ D

def check_result():
#count stop timer and check timer
    global D, num_stop, num_win, stop
    if stop==False:
        num_stop+=1
        if not(int(D)):
            num_win+=1

def ini_vari():
#initialize the variables
    global tenthsec, num_stop, num_win, stop
    timer.stop()
    tenthsec=0
    num_stop=0
    num_win=0
    stop=False
  
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
#Start button
    global stop
    timer.start()
    stop=False

def button_stop():
#Stop button
    global stop
    timer.stop()
    check_result()
    stop=True

def button_reset():
#Reset button
    timer.stop()
    ini_vari()

# define event handler for timer with 0.1 sec interval
def timer_tenthsec():
    global tenthsec
    tenthsec+=1

# define draw handler
def draw_game(canvas):
    global num_win, num_stop
    canvas.draw_text( format(tenthsec), (75, 125), 50, 'Red')
    canvas.draw_text( str(num_win)+ '/' + str(num_stop), (250, 40), 20, 'Blue')
    
# create frame
frame = simplegui.create_frame('Stop the watch', 300, 200)

# register event handlers
#buttons handlers
button_start = frame.add_button('Start', button_start)
button_stop = frame.add_button('Stop', button_stop)
button_reset = frame.add_button('Reset', button_reset)

#timer handlers
timer = simplegui.create_timer(100, timer_tenthsec)

#draw handlers
frame.set_draw_handler(draw_game)
#frame.set_draw_handler(draw_result)

# start frame
frame.start()
num_stop=0
num_win=0
tenthsec=0

# Please remember to review the grading rubric
