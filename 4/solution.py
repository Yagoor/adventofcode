class ScratchCards:
    winning_numbers = None
    elf_numbers = None
    amount = 0

    def __init__(self, winning_numbers, elf_numbers):
        self.winning_numbers = winning_numbers
        self.elf_numbers = elf_numbers
        self.amount = 1

    def matching_numbers(self):
        return self.elf_numbers.intersection(self.winning_numbers)

    def value(self):
        intersection = self.elf_numbers.intersection(self.winning_numbers)
        if len(intersection) > 0:
            return (2 ** (len(intersection) - 1)) * self.amount
        return 0

    def add(self, val):       
        self.amount += val


with open('input', 'r') as fp:
    data = fp.readlines()

cards = []
modified_cards = []
for card in data:
    card = card.strip()

    split_1 = card.split(":")

    game = split_1[0]
    numbers = split_1[1]

    split_2 = numbers.split("|")
    winning_numbers = split_2[0]
    elf_numbers = split_2[1]

    winning_numbers = winning_numbers.replace("  ", " ").strip().split(" ")
    elf_numbers = elf_numbers.replace("  ", " ").strip().split(" ")

    cards.append(ScratchCards(set(winning_numbers), set(elf_numbers)))
    modified_cards.append(ScratchCards(set(winning_numbers), set(elf_numbers)))

sum = 0
for i in range(len(cards)):
    card = cards[i]
    for j in range(len(card.matching_numbers())):
        if i + j + 1 > len(cards):
            continue
        modified_cards[i + j + 1].add(modified_cards[i].amount)
    sum += card.value()

print("Sum 1", sum)

sum = 0
for i in range(len(modified_cards)):
    card = modified_cards[i]
    sum += card.amount 

print("Sum 2", sum)
