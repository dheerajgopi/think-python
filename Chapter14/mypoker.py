import random
class Card(object):
    '''defines a card

    attributes : suit, rank'''


    card_suit = {0:'Clubs', 1:'Diamonds', 2:'Hearts', 3:'Spades'}
    card_rank = {0:None, 1:'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King'}


    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return '%s of %s' %(self.card_rank[self.rank], self.card_suit[self.suit])


    def __cmp__(self,other):
        '''returns 1 : if self > other
                  -1 : if self < other
                   0 : if self = other'''
        card1 = self.suit, self.rank
        card2 = other.suit, other.rank
        return cmp(card1,card2)


class Deck(object):
    '''defines a deck of 52 cards'''


    def __init__(self):
        self.cards = [Card(suit,rank) for suit in range(4) for rank in range(1,14)]


    def __str__(self):
        deck = [str(card) for card in self.cards]
        return '\n'.join(deck)


    def pop_card(self):
        return self.cards.pop()


    def add_card(self,card):
        self.cards.append(card)


    def shuffle(self):
        random.shuffle(self.cards)


    def sort(self):
        self.cards.sort()


    def move_cards(self, hand, num):
        '''move 'num' number of cards from 'self' to 'hand'
        self & hand can be Deck object & Hand object or vice-versa'''

        for i in range(num):
            hand.add_card(self.pop_card())


    def deal_hands(self,num_hands,num_cards):
        '''deals 'num_card' number of cards to 'num_hands' number
        of hands from the deck 'self' 
        returns a dict of hands with hand.label as its key'''
        hand_dict = {}
        for i in range(num_hands):
            hand = Hand('Hand'+str(i))
            self.move_cards(hand,num_cards)
            hand_dict['hand'+str(i)] = hand
        print hand_dict.keys()
        return hand_dict


class Hand(Deck):
    '''represents a hand of cards

    attributes : label'''


    def __init__(self, label = ''):
        self.cards = []
        self.label = label
