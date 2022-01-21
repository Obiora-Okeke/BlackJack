#/usr/bin/python
# -*- coding: utf-8 -*-
import random
suits = ['♠','♥','♦','♣'] # Feel free to use these symbols to represent the
points = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'A':11}
#specialpoints is the same dictionary as before but include a value of 1 for and Ace
specialpoints = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'A':11, 'Ace':1}
#suits = ['spade','heart','diamond','club'] # Feel free to use these symbols to represent the different suits.
class Card(object):

   def __init__(self, suit, rank):


        self.rank = rank
        self.suit = suit
        self.points = specialpoints[rank]
        pass # replace this
   def __str__(self):
       return( '{} of {} - {}'.format(self.rank,self.suit,str(self.points))) # replace this line
openDeck = []
class CardCollection(object):

   def __init__(self):
       self.cards = []
   def add_card(self, card):
       self.cards.append(str(card))
       return (self.cards)
       #pass # replace this line
   def draw_card(self):
       retract = self.cards.pop(0)
       return (retract)
        # replace this, must remove and return a Card instance from self.cards

   def remove(self, index):#this function will help me the whole Ace value being 1 or 11
       rem = self.cards.pop(index)
       return(rem)


   def make_deck(self):

       for i in suits:
         for j in points:


           self.cards.append(Card(i,j))

       random.shuffle(self.cards)
       return(self.cards)

       #pass   # replace this, initialize self.cards with a fresh list of the 52 playing cards in random order.
   def value(self):
       total = 0
       for i in self.cards:
         newli = i.split()
         total +=specialpoints[newli[0]]
       return(total)

       #return 0 # replace this, must return an int representing the total
                # value of cards in this collection


def main():
    deck = CardCollection()
    deck.make_deck() # initialize a fresh deck
    player_hand = CardCollection()
    dealer = CardCollection()
    card = deck.draw_card()
    SR = str(card).split()
    player_hand.add_card(Card(SR[2],SR[0]))
    print("you drew",card )
    print("sum: ", player_hand.value())

    while(player_hand.value() != 21 and player_hand.value()< 22):
      answer = input("Do you want another card? (y/n)")
      if answer == 'y':
        card = deck.draw_card()
        SR = str(card).split()
        if SR[0] == "A" and player_hand.value() > 10:
          player_hand.add_card(Card(SR[2],"Ace"))
          print("you drew",card )


        else:
          player_hand.add_card(Card(SR[2],SR[0]))
          print("you drew",card )


          if player_hand.value()> 21:

            for i in player_hand.cards:
              checkli = i.split()

              if checkli[0] =='A':
                player_hand.remove(player_hand.cards.index(i))
                player_hand.add_card(Card(checkli[2],"Ace"))

              else:
                  pass
        print("sum: ", player_hand.value())
      elif answer == "n":
        while(dealer.value()<=17):
          Dcard = deck.draw_card()
          DSR = str(Dcard).split()
          if DSR[0] == "A" and dealer.value() > 10:
            dealer.add_card(Card(DSR[2],"Ace"))
            print("Computer drew",card )

          else:
            dealer.add_card(Card(DSR[2],DSR[0]))
            print("Computer drew",Dcard )
            if dealer.value() >21:
              for i in dealer.cards:
                Dcheckli = i.split()
                if Dcheckli[0] == 'A':
                  dealer.remove(dealer.cards.index(i))
                  dealer.add_card(Card(Dcheckli[2],"Ace"))
                else:
                  pass
          print("sum: ", dealer.value())
        break

    if player_hand.value() < dealer.value() and dealer.value() <=21 or player_hand.value()> 21:
      print("Computer wins")
    elif player_hand.value() > dealer.value() or dealer.value() > 21:
      print("You win")
    else:
      print("The game is a push, nobody wins")
   # complete the main method
if __name__ == "__main__":
   main()
