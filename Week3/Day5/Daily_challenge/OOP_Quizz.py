red = '\033[91m'
reset = '\033[0m'
green = '\033[92m'
blue = '\033[94m'
color = red

# Quiz:

q1 = 'What is a class?'
a1 = 'A class is a blueprint for creating objects. Objects have properties and methods(functions) associated with them. Almost everything in Python is an object.'

q2 = 'What is instance?'
a2 = 'An instance is a specific object created from a class, having its own unique data and behavior based on the class definition.'

q3 = 'What is encapsulation?'
a3 = 'Encapsulation is the concept that binds data (attributes) and methods (functions), and that operate on the data within a class, hiding the internal implementation details from the outside world.'

q4 = 'What is abstraction?'
a4 = 'Abstraction is an OOP concept that focuses only on relevant data of an object. It hides the background details and emphasizes the essential features necessary for the end result.'

q5 = 'What is inheritance?'
a5 = 'Inheritance is an OOP concept that allows a class to inherit methods and properties from another class.'

q6 = 'What is multiple inheritance?'
a6 = 'Multiple inheritance is when a class can inherit attributes and methods from more than one parent class.'

q7 = 'What is polymorphism?'
a7 = 'Polymorphism allows objects of different classes to be treated as objects of a common superclass, enabling them to be used interchangeably and respond to the same interface.'

q8 = 'What is method resolution order or MRO?'
a8 = 'MRO is the order in which Python looks for a method in a hierarchy of classes.'

# Deck of Cards
import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q', 'K']
    
    @classmethod
    def card_name(cls):  
        return f"{random.choice(Card.values)} of {random.choice(Card.suits)}" 

class Deck:
    NUM_CARDS = 52

    def __init__(self):
        self.cards = Deck.build_deck()

    @staticmethod
    def build_deck():
        cards = set()
        while len(cards) < Deck.NUM_CARDS: 
            random_card = Card.card_name()
            cards.add(random_card)
        return list(cards)     

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop() 
        else:
            print(red + "No cards left in the deck!" + reset)         

deck = Deck()
for _ in range(5):
    print('Cards in deck: ' + green + str(len(deck.cards)) + reset)
    deck.shuffle()
    print(', '.join(deck.cards[:5]))
    print(blue + deck.deal() + reset)
print("++++++++++++++++++++++")
deck2 = Deck()
for _ in range(53):
    deck2.shuffle()
    deck2.deal()