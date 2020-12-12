import random
# Game is played from 9 up through Ace of each suit
cards = ['9S', '10S', 'JS', 'QS', 'KS', 'AS', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
         '9D', '10D', 'JD', 'QD', 'KD', 'AD']


# Each of the 4 players gets a hand of 5 unique cards with 1 final card face up on table (3 are face down and unused)
Dealt_Cards = random.sample(cards, 21)


Player_1_Hand = random.sample(Dealt_Cards, 5)
for i in range(5):
    Dealt_Cards.remove(Player_1_Hand[i])
Player_2_Hand = random.sample(Dealt_Cards, 5)
for i in range(5):
    Dealt_Cards.remove(Player_2_Hand[i])
Player_3_Hand = random.sample(Dealt_Cards, 5)
for i in range(5):
    Dealt_Cards.remove(Player_3_Hand[i])
Player_4_Hand = random.sample(Dealt_Cards, 5)
for i in range(5):
    Dealt_Cards.remove(Player_4_Hand[i])
Flipped_Card = random.sample(Dealt_Cards, 1)


#Displays the 21 cards chosen for the round
print(Flipped_Card, Player_1_Hand, Player_2_Hand, Player_3_Hand, Player_4_Hand)


#The flipped card is important. The suit of this card can help determine which suit is trump or clincher suit for the round

def spade_flipped(Flipped_Card):
    if 'S' in Flipped_Card:
        return True
def club_flipped(Flipped_Card):
    if 'C' in Flipped_Card:
        return True
def heart_flipped(Flipped_Card):
    if 'H' in Flipped_Card:
        return True
def diamond_flipped(Flipped_Card):
    if 'D' in Flipped_Card:
        return True


#These lists will be populated with point values for each suit in the order [spades, clubs, hearts, diamonds]
#cards have different pt values depending on which suit is clincher

P1_Suits_Value = [0, 0, 0, 0]
P2_Suits_Value = [0, 0, 0, 0]
P3_Suits_Value = [0, 0, 0, 0]
P4_Suits_Value = [0, 0, 0, 0]

declared_suit = ''


def declared_clincher(declared_suit):
    spades_declared = False
    clubs_declared = False
    hearts_declared = False
    diamonds_declared = False


# Definitions are created for each possible clincher suit


def Spades_Clincher_Values(Player_1_Hand):
    if 'JS' in Player_1_Hand:
        P1_Suits_Value[0] += 8
    if 'JC' in Player_1_Hand:
        P1_Suits_Value[0] += 7
    if 'AS' in Player_1_Hand:
        P1_Suits_Value[0] += 6
    if 'KS' in Player_1_Hand:
        P1_Suits_Value[0] += 5
    if 'QS' in Player_1_Hand:
        P1_Suits_Value[0] += 4
    if '10S' in Player_1_Hand:
        P1_Suits_Value[0] += 3
    if '9S' in Player_1_Hand:
        P1_Suits_Value[0] += 2
    if 'AC' in Player_1_Hand:
        P1_Suits_Value[0] += 1
    if 'AH' in Player_1_Hand:
        P1_Suits_Value[0] += 1
    if 'AD' in Player_1_Hand:
        P1_Suits_Value[0] += 1
    return P1_Suits_Value


Spades_Clincher_Values(Player_1_Hand)


def Clubs_Clincher_Values(Player_1_Hand):
    if 'JC' in Player_1_Hand:
        P1_Suits_Value[1] += 8
    if 'JS' in Player_1_Hand:
        P1_Suits_Value[1] += 7
    if 'AC' in Player_1_Hand:
        P1_Suits_Value[1] += 6
    if 'KC' in Player_1_Hand:
        P1_Suits_Value[1] += 5
    if 'QC' in Player_1_Hand:
        P1_Suits_Value[1] += 4
    if '10C' in Player_1_Hand:
        P1_Suits_Value[1] += 3
    if '9C' in Player_1_Hand:
        P1_Suits_Value[1] += 2
    if 'AS' in Player_1_Hand:
        P1_Suits_Value[1] += 1
    if 'AH' in Player_1_Hand:
        P1_Suits_Value[1] += 1
    if 'AD' in Player_1_Hand:
        P1_Suits_Value[1] += 1
    return P1_Suits_Value


Clubs_Clincher_Values(Player_1_Hand)


def Hearts_Clincher_Values(Player_1_Hand):
    if 'JH' in Player_1_Hand:
        P1_Suits_Value[2] += 8
    if 'JD' in Player_1_Hand:
        P1_Suits_Value[2] += 7
    if 'AH' in Player_1_Hand:
        P1_Suits_Value[2] += 6
    if 'KH' in Player_1_Hand:
        P1_Suits_Value[2] += 5
    if 'QH' in Player_1_Hand:
        P1_Suits_Value[2] += 4
    if '10H' in Player_1_Hand:
        P1_Suits_Value[2] += 3
    if '9H' in Player_1_Hand:
        P1_Suits_Value[2] += 2
    if 'AC' in Player_1_Hand:
        P1_Suits_Value[2] += 1
    if 'AS' in Player_1_Hand:
        P1_Suits_Value[2] += 1
    if 'AD' in Player_1_Hand:
        P1_Suits_Value[2] += 1
    return P1_Suits_Value


Hearts_Clincher_Values(Player_1_Hand)


def Diamonds_Clincher_Values(Player_1_Hand):
    if 'JD' in Player_1_Hand:
        P1_Suits_Value[3] += 8
    if 'JH' in Player_1_Hand:
        P1_Suits_Value[3] += 7
    if 'AD' in Player_1_Hand:
        P1_Suits_Value[3] += 6
    if 'KD' in Player_1_Hand:
        P1_Suits_Value[3] += 5
    if 'QD' in Player_1_Hand:
        P1_Suits_Value[3] += 4
    if '10D' in Player_1_Hand:
        P1_Suits_Value[3] += 3
    if '9D' in Player_1_Hand:
        P1_Suits_Value[3] += 2
    if 'AC' in Player_1_Hand:
        P1_Suits_Value[3] += 1
    if 'AS' in Player_1_Hand:
        P1_Suits_Value[3] += 1
    if 'AH' in Player_1_Hand:
        P1_Suits_Value[3] += 1
    return P1_Suits_Value


Diamonds_Clincher_Values(Player_1_Hand)

#Displays the pts value of Player 1s hand for each possible clincher suit (clincher suit for the round has yet to be determined)
#This is done so Player 1 can decide whether to call a certain suit clincher is a good decision

print(P1_Suits_Value)

def declare_suit_flipped_P1(spade_flipped, club_flipped, heart_flipped, diamond_flipped, P1_Suits_Value, declared_suit):
    #after experimenting with generating hands, 16 pts with the current point system seems to be a decent cutoff for declaring which suit
    #will be clincher for the round

    if spade_flipped and P1_Suits_Value[0] >= 16:
        declared_suit += 'spades'
    if club_flipped and P1_Suits_Value[1] >= 16:
        declared_suit += 'clubs'
    if heart_flipped and P1_Suits_Value[2] >= 16:
        declared_suit += 'hearts'
    if diamond_flipped and P1_Suits_Value[3] >= 16:
        declared_suit += 'diamonds'
    else:
        return None

    return declared_suit


declare_suit_flipped_P1(spade_flipped, club_flipped, heart_flipped, diamond_flipped, P1_Suits_Value, declared_suit)

print(declared_suit)


