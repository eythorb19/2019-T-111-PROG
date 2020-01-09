import random

JACK = 'J'
QUEEN = 'Q'
KING = 'K'
ACE = 'A'
FACE_VALUE = 10 # The value of jack, queen and king
ACE_VALUE = 11  # The value of ace
MAX_HAND_VALUE = 21 # maximum sum of cards of a hand before busted
MAX_HAND_CARDS = 5  # maximum number of cards in a hand
MORE_CARDS_IF_LESS = 17 # player receives more cards if value of hand is less than this value
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

def get_card_value(card):
    ''' Returns the value of the given card '''
    if card in ['2','3','4','5','6','7','8','9','10']:
        return int(card)
    elif card in [JACK,QUEEN,KING]:
        return FACE_VALUE
    else:
        return ACE_VALUE 

def deal(deck):
    ''' Deals cards from the given deck to a hand until the sum of cards >= 17 or number of cards = 5
        The dealt cards are removed from the deck at the right end, and returned in a list '''
    sum = 0
    cards = 0
    hand = []
    while sum < MORE_CARDS_IF_LESS and cards < MAX_HAND_CARDS:
        card = deck.pop()
        cards += 1
        hand.append(card)
        sum += get_card_value(card)
    return hand

def get_hand_value(hand):
    ''' Returns the value of the given hand '''
    sum = 0
    for card in hand:
        sum += get_card_value(card)
    return sum

def get_winner(player_hand, dealer_hand):
    ''' Given two lists of cards (player_hand, dealer_hand), 
        returns either WINNER_DEALER or WINNER_PLAYER,
        signifying the dealer_hand or the player_hand as a winner, respectively '''
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    
    if player_value > MAX_HAND_VALUE:
        return WINNER_DEALER
    elif dealer_value > MAX_HAND_VALUE:
        return WINNER_PLAYER
    elif player_value <= dealer_value:
        return WINNER_DEALER
    else:
        return WINNER_PLAYER
    
def print_hands(player_hand, dealer_hand):
    ''' Prints the given hands '''
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    print('Player: {} -> {}'.format(player_value, " ".join(player_hand)))
    print('Dealer: {} -> {}'.format(dealer_value, " ".join(dealer_hand))) 
    
def print_winner(winner):
    if winner == WINNER_PLAYER:
        print("Player won!")
    else:
        print("Dealer won!")

def print_total_wins(player_wins, dealer_wins):    
    print("Player won {} times".format(player_wins))
    print("Dealer won {} times".format(dealer_wins))
    
def play_game(deck):
    player_hand = deal(deck)
    dealer_hand = deal(deck)
    print_hands(player_hand, dealer_hand)
    winner = get_winner(player_hand, dealer_hand)
    print_winner(winner)
    return winner

def game_loop(deck):
    ''' Plays the game until the user quits '''
    player_wins = 0
    dealer_wins = 0
    count = 0
    while count < HOW_OFTEN:
        winner = play_game(deck)
        if winner == WINNER_PLAYER:
            player_wins += 1
        else:
            dealer_wins += 1
        count += 1

    print_total_wins(player_wins, dealer_wins)


# Main program starts here
if __name__ == "__main__":
    seed = int(input('Random seed: '))
    random.seed(seed)
    deck = initialize_deck()
    #print(deck)
    game_loop(deck)
