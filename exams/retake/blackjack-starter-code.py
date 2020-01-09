import random

JACK = 'J'
QUEEN = 'Q'
KING = 'K'
ACE = 'A'
FACE_VALUE = 10 # The value of jack, queen and king
ACE_VALUE = 11  # The value of ace
MAX_HAND_VALUE = 21 # maximum sum of cards of a hand before busted
MAX_HAND_CARDS = 5  # maximum number of cards in a hand
HOW_OFTEN = 5   # the number of times the game is played

WINNER_PLAYER = 0   # means player wins a game
WINNER_DEALER = 1   # means dealer wins a game

def initialize_deck():
    ''' Initializes a 52-card deck '''
    deck = []
    for _ in range(0,4):
        for card in range(2,11):
            deck.append(str(card))
        deck.append(JACK)
        deck.append(QUEEN)
        deck.append(KING)
        deck.append(ACE)
    
    random.shuffle(deck)
    return(deck)


def deal(deck):
    ''' Deals cards from the given deck to a hand until the sum of cards >= 17 or number of cards = 5
        The dealt cards are removed from the deck at the right end, and returned in a list '''
    pass


def get_winner(player_hand, dealer_hand):
    ''' Given two lists of cards (player_hand, dealer_hand), 
        returns either WINNER_DEALER or WINNER_PLAYER,
        signifying the dealer_hand or the player_hand as a winner, respectively '''
    pass


# Main program starts here
if __name__ == "__main__":
    seed = int(input('Random seed: '))
    random.seed(seed)
    deck = initialize_deck()
