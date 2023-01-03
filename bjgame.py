############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. 
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

user = []
com = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calc(temp):
    if(sum(temp) == 21 and len(temp) == 2):
        return 1

    if(11 in temp and sum(temp) > 21):
        temp.remove(11)
        temp.append(1)

    return sum(temp)

def compare(tmpuser,tmpcom):
    if(tmpuser == 1):
        return 'blackjack! win'
    elif(tmpcom == 1):
        return "dealer's blackjack lose"
    elif(tmpcom > 21):
        return 'win'
    elif(tmpuser > 21):
        return 'lose'
    elif(tmpuser> tmpcom):
        return 'win'
    else:
        return 'lose'


for i in range(2):
        dealuser = cards[random.randint(0,len(cards)-1)]
        user.append(dealuser)
        dealcom = cards[random.randint(0,len(cards)-1)]
        com.append(dealcom)

plays = True

while input("let's plays game! (y or n): ").lower() == 'y':
    while plays:
        print(user, 'is your cards.')

        print(calc(user), 'is your total points.')

        if(calc(user) == 1 or calc(user) > 21):
            plays = False
        else:
            choice = input('another cards (y or n): ').lower()
            if(choice =='y'):
                dealuser = cards[random.randint(0,len(cards)-1)]
                user.append(dealuser)
            else:
                plays = False

    while calc(com) < 17:
        dealcom = cards[random.randint(0,len(cards)-1)]
        com.append(dealcom)

    print(compare(calc(user),calc(com)))



