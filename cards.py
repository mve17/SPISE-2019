# Daniel Ellison 2019
# Python 3.7.2
# cards.py

##################################### Sample Usage #####################################

# Card object #####################################
    # Initialize card
        # >>> my_card = Card('5', 'Hearts')
        # >>> my_card
        # <Card object: 5 of Hearts>
    # Get attributes
        # >>> my_card.get_value()
        # '5'
        # >>> my_card.get_suit()
        # 'Hearts'

# Deck object #####################################
    # Initialize deck (NOTE: deck is initialized unshuffled in Bicycle order. NO JOKERS)
        # >>> my_deck = Deck()
    # Shuffle deck (NOTE: shuffle is a random permutation)
        # >>> my_deck.shuffle()
    # Deal card (no replacement)
        # >>> my_deck.deal_card()
        # <Card object: A of Hearts>
    # Number of cards left
        # >>> my_deck.get_cards_remaining()
        # 51
    # Combine the discard pile with the rest of the cards
        # >>> my_deck.combine()
        # >>> my_deck.get_cards_remaining()
        # 52

# ADVANCED DECK OBJECT USAGE #####################################
    # Initialize object using 2 decks, 8 jokers, and Phoenix card order
        # >>> my_deck = Deck(number=2, jokers=8, order='Phoenix')
    # Shuffle with a realistic riffle shuffle
        # >>> my_deck.riffle_shuffle()
    # Perform a perfect in shuffle (Faro) (Requires even number of cards)
        # >>> my_deck.in_faro_shuffle()
    # Perform a perfect out shuffle (Faro) (Requires even number of cards)
        # >>> my_deck.out_faro_shuffle()
    # Get number of cards discarded
        # >>> my_deck.get_discard_number()
        # 0
    # Get deck and discard pile
        # >>> my_deck.get_deck()
        # [<deck>, <discard_pile>]
    # Create a custom deck
        # >>> my_cards = [Card('A', 'Spades'), Card('2', 'Clubs'), Card('6', 'Diamonds')]
        # >>> my_custom_deck = Deck(deck=my_cards)
        # >>> my_custom_deck.get_deck()
        # [[<Card object: A of Spades>, <Card object: 2 of Clubs>, <Card object: 6 of Diamonds>], []]


########################################################################################
    
import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return '<Card object: {} of {}>'.format(self.value, self.suit)
    def get_value(self):
        return self.value
    def get_suit(self):
        return self.suit

class Deck():
    def __init__(self, number=1, jokers=0, order='Bicycle', deck=[]):
        self.number = number
        self.jokers = 0
        self.order = order
        
        self.discard_pile = []

        value_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = deck
        if self.deck == []:
            if self.order == 'Phoenix':
                for i in range(self.number):
                    self.deck += [Card(value, 'Spades') for value in value_order]
                    self.deck += [Card(value, 'Hearts') for value in value_order]
                    self.deck += [Card(value, 'Diamonds') for value in value_order[::-1]]
                    self.deck += [Card(value, 'Clubs') for value in value_order[::-1]]
            else:
                for i in range(self.number):
                    self.deck += [Card(value, 'Hearts') for value in value_order]
                    self.deck += [Card(value, 'Clubs') for value in value_order]
                    self.deck += [Card(value, 'Diamonds') for value in value_order[::-1]]
                    self.deck += [Card(value, 'Spades') for value in value_order[::-1]]           
            self.deck += [Card('?', 'JOKER') for i in range(self.jokers)]

    def shuffle(self):
        random.shuffle(self.deck)
        
    def riffle_shuffle(self):
        top_packet_size = len(self.deck)//2 + random.randint(-len(self.deck)//10, len(self.deck)//10)
        top_packet = self.deck[:top_packet_size]
        bot_packet = self.deck[top_packet_size:]
        shuffled_pile = []
        while len(top_packet) > 0 and len(bot_packet) > 0:
            if len(bot_packet) > 0:
                weave_size = random.randint(1,4)
                if len(bot_packet) < weave_size:
                    weave_size = len(bot_packet)
                shuffled_pile += bot_packet[-weave_size:]
                bot_packet = bot_packet[:-weave_size]
            if len(top_packet) > 0:
                weave_size = random.randint(1,4)
                if len(top_packet) < weave_size:
                    weave_size = len(top_packet)
                shuffled_pile += top_packet[-weave_size:]
                top_packet = top_packet[:-weave_size]
        self.deck = shuffled_pile

    def in_faro_shuffle(self):
        if len(self.deck) % 2 == 0:
            top_packet = self.deck[:len(self.deck)//2]
            bot_packet = self.deck[len(self.deck)//2:]
            shuffled_pile = []
            for i in range(len(top_packet)):
                shuffled_pile.append(top_packet[-1])
                top_packet = top_packet[:-1]
                shuffled_pile.append(bot_packet[-1])
                bot_packet = bot_packet[:-1]
            self.deck = shuffled_pile
        else:
            print('Deck must have an even number of cards for a Faro shuffle')

    def out_faro_shuffle(self):
        if len(self.deck) % 2 == 0:
            top_packet = self.deck[:len(self.deck)//2]
            bot_packet = self.deck[len(self.deck)//2:]
            shuffled_pile = []
            for i in range(len(top_packet)):
                shuffled_pile.append(bot_packet[-1])
                bot_packet = bot_packet[:-1]
                shuffled_pile.append(top_packet[-1])
                top_packet = top_packet[:-1]
            self.deck = shuffled_pile
        else:
            print('Deck must have an even number of cards for a Faro shuffle')

    def deal_card(self):
        if len(self.deck) == 0:
            self.combine()
            self.shuffle()
        top_card = self.deck[0]
        self.deck = self.deck[1:]
        self.discard_pile.append(top_card)
        return top_card

    def get_cards_remaining(self):
        return len(self.deck)

    def get_discard_number(self):
        return len(self.discard_pile)
    
    def combine(self):
        self.deck += self.discard_pile
        self.discard_pile = []

    def get_deck(self):
        return [self.deck, self.discard_pile]
                
