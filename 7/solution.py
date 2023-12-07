class Hand:
    cards = []
    bet = 0

    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        self.power = self.get_power()
        self.power_2 = self.get_power_2()

    def get_power(self):
        dict = { }
        for x in self.cards:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1

        iterator = iter(sorted(dict.items(), key=lambda x:x[1], reverse=True))
        item_1 = next(iterator)
        # Five of a kind, where all five cards have the same label: AAAAA
        if item_1[1] == 5:
            return 7
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if item_1[1] == 4:
            return 6
        
        item_2 = next(iterator)
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if item_1[1] == 3 and item_2[1] == 2:
            return 5

        item_3 = next(iterator)
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        if item_1[1] == 3 and item_2[1] == 1 and item_3[1] == 1:
            return 4

        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        if item_1[1] == 2 and item_2[1] == 2 and item_3[1] == 1:
            return 3
        
        item_4 = next(iterator)
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        if item_1[1] == 2 and item_2[1] == 1 and item_3[1] == 1 and item_4[1] == 1:
            return 2
        
        # High card, where all cards' labels are distinct: 23456
        return 1

    def get_power_2(self):
        dict = { }
        j_num = 0
        for x in self.cards:
            if x == 'J':
                j_num += 1
            else:
                if x in dict:
                    dict[x] += 1
                else:
                    dict[x] = 1


        iterator = iter(sorted(dict.items(), key=lambda x:x[1], reverse=True))
        item_1 = next(iterator, None)

        # Five of a kind, where all five cards have the same label: AAAAA
        if j_num == 5: #JJJJJ
            return 7        
        if item_1[1] == 5: # AAAAA
            return 7
        if item_1[1] == 4 and j_num == 1: #AAAJA
            return 7
        if item_1[1] == 3 and j_num == 2: #AAAJJ
            return 7
        if item_1[1] == 2 and j_num == 3: #AAJJJ
            return 7
        if item_1[1] == 1 and j_num == 4: #AJJJJ
            return 7
        
        item_2 = next(iterator, None)
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if item_1[1] == 4:  #AA8AA
            return 6
        if item_1[1] == 2 and item_2[1] == 2 and j_num == 2:  #A8AJJ
            return 6        
        if item_1[1] == 3 and item_2[1] == 1 and j_num == 1:  #A8AAJ
            return 6
        if item_1[1] == 2 and item_2[1] == 1 and j_num == 2:  #A8AJJ
            return 6
        if item_1[1] == 1 and item_2[1] == 1 and j_num == 3:  #A8JJJ
            return 6
                
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if item_1[1] == 3 and item_2[1] == 2: # 23332
            return 5
        if item_1[1] == 2 and item_2[1] == 2 and j_num == 1: # 233J2
            return 5

        item_3 = next(iterator, None)
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        if item_1[1] == 3 and item_2[1] == 1 and item_3[1] == 1: # TTT98
            return 4
        if item_1[1] == 2 and item_2[1] == 1 and item_3[1] == 1 and j_num == 1: # TTJ98
            return 4
        if item_1[1] == 1 and item_2[1] == 1 and item_3[1] == 1 and j_num == 2: # TJJ98
            return 4
        
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        if item_1[1] == 2 and item_2[1] == 2 and item_3[1] == 1: #23432
            return 3     

        item_4 = next(iterator, None)
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        if item_1[1] == 2 and item_2[1] == 1 and item_3[1] == 1 and item_4[1] == 1: #A23A4
            return 2
        if j_num == 1:
            return 2
                                
        # High card, where all cards' labels are distinct: 23456
        return 1

    def is_stronger(self, another):
        card_to_individual_power = {
            'A' : 13,
            'K' : 12,
            'Q' : 11,
            'J' : 10,
            'T' : 9,
            '9' : 8,
            '8' : 7,
            '7' : 6,
            '6' : 5,
            '5' : 4,
            '4' : 3,
            '3' : 2,
            '2' : 1,
        }        
        if self.power > another.power:
            return True
        elif self.power < another.power:
            return False    
        else:
            for x, y in zip(self.cards, another.cards):
                if card_to_individual_power[x] > card_to_individual_power[y]:
                    return True
                elif card_to_individual_power[x] < card_to_individual_power[y]:
                    return False
                else:
                    continue

    def is_stronger_2(self, another):
        card_to_individual_power = {
            'A' : 13,
            'K' : 12,
            'Q' : 11,
            'T' : 10,
            '9' : 9,
            '8' : 8,
            '7' : 7,
            '6' : 6,
            '5' : 5,
            '4' : 4,
            '3' : 3,
            '2' : 2,
            'J' : 1,
        }        
        if self.power_2 > another.power_2:
            return True
        elif self.power_2 < another.power_2:
            return False    
        else:
            for x, y in zip(self.cards, another.cards):
                if card_to_individual_power[x] > card_to_individual_power[y]:
                    return True
                elif card_to_individual_power[x] < card_to_individual_power[y]:
                    return False
                else:
                    continue

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

hands = []
for entry in data:
    cards, bet = map(str, entry.split(' '))
    hands.append(Hand(cards, int(bet)))

for x in hands:
    wins = 0
    for y in hands:
        if x == y:
            # Skip myself
            continue

        if x.is_stronger(y):
            wins += 1

    x.wins = wins

hands.sort(key=lambda x: x.wins)
sum = 0
for i in range(len(hands)):
    sum += (hands[i].bet * (i + 1))

print("Sum 1", sum)


hands = []
for entry in data:
    cards, bet = map(str, entry.split(' '))
    hands.append(Hand(cards, int(bet)))

for x in hands:
    wins = 0
    for y in hands:
        if x == y:
            # Skip myself
            continue

        if x.is_stronger_2(y):
            wins += 1

    x.wins = wins

hands.sort(key=lambda x: x.wins)
sum = 0
for i in range(len(hands)):
    sum += (hands[i].bet * (i + 1))

print("Sum 2", sum)
