# Mini-project #6 - Blackjack
# week 6
# http://www.codeskulptor.org/#user25_af1DGqaM40_1.py

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
message = ''
score = 0
deck = None
player_hand = None
dealer_hand = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = 'Hand contains'
        for card in self.cards:
            rep += ' ' + str(card)
        return rep

    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ace = False
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = True      
        if ace and value + 10 <= 21:
            value += 10    
        return value
   
    def draw(self, canvas, pos):
        c = 0
        for card in self.cards:
            card.draw(canvas, [pos[0] + CARD_SIZE[0] * c, pos[1]])                  
            c += 1

 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        rep = 'Deck contains'
        for card in self.cards:
            rep += ' ' + str(card)
            
        return rep

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, message
    global dealer_hand, player_hand, score
    
    if in_play:
        score -= 1

    # create and shuffle the deck
    deck = Deck()
    deck.shuffle()
    
    
    player_hand, dealer_hand = Hand(), Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    in_play = True
    outcome = "Hit or Stand?"
    message = ''
    

def hit():
    # if the hand is in play, hit the player
    global outcome, in_play, message, score
        
    if not in_play:
        return
    if player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:

        outcome = "New Deal?"
        message = "You busted!!"
        score -= 1
        in_play = False
        
    
       
def stand():
    global outcome, in_play, message, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if not in_play:
        return
    
    if player_hand.get_value() > 21:
        message = "You busted!!"
        score -= 1
        in_play = False
        return
    
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        
    if dealer_hand.get_value() > 21:
        message = "The Dealer has busted!!"
        score += 1
    else:
        if player_hand.get_value() <= dealer_hand.get_value():
            message = "The dealer wins!!!"
            score -= 1
        else:
            message = "You win!!!"
            score += 1
     
    # assign a message to outcome, update in_play and score
    outcome = "New Deal?"
    in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text("Blackjack Time!!", (50, 50), 40, "Red")
    canvas.draw_text(outcome, (250, 350), 25, "Black")
    
    canvas.draw_text("Player", (75, 350), 25, "Black")
    canvas.draw_text("Dealer", (75, 150), 25, "Black")
    
    canvas.draw_text(message, (250, 150), 25, "Black")
    
    canvas.draw_text("Score: " + str(score), 
                     (220, 575), 30, "Black")
    
    player_hand.draw(canvas, [75, 400])
    dealer_hand.draw(canvas, [75, 200])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [75 + CARD_BACK_CENTER[0],
                           200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
                                     

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()

# get things rolling
frame.start()


# remember to review the gradic rubric