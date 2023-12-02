class Game:
    index = 0

    class Subset:
        red = 0
        green = 0
        blue = 0

        def __init__(self, red, green, blue):
            self.red = red
            self.green = green
            self.blue = blue

        def is_valid(self, red, green, blue):
            if self.red > red or \
                self.green > green or \
                self.blue > blue:
                return False
            
            return True

    subsets = []

    def __init__(self, index):
        self.index = index
        self.subsets = []
    
    def add_subset(self, red, blue, green):
        self.subsets.append(Game.Subset(red, blue, green))

    def is_valid(self):
        max_red = 12
        max_green = 13
        max_blue = 14

        for subset in self.subsets:
            if not subset.is_valid(max_red, max_green, max_blue):
                return False

        return True

    def power(self):
        red = 0
        green = 0
        blue = 0

        for subset in self.subsets:
            if subset.red > red:
                red = subset.red
            if subset.green > green:
                green = subset.green
            if subset.blue > blue:
                blue = subset.blue
                               
        return red * green * blue

    def __str__(self) -> str:
        return "{}".format(self.index)

with open('input', 'r') as fp:
    data = fp.readlines()

games = []
for line in data:
    line = line.strip()
    split_1 = line.split(':')

    split_2 = split_1[0].split(" ")

    game_index = int(split_2[1])

    game = Game(game_index)
    split_3 = split_1[1].split(';')
    for subset in split_3:
        red = 0
        green = 0
        blue = 0
        split_4 = subset.split(",")
        for entry in split_4:
            split_5 = entry.split(" ")
            if split_5[2] == "red":
                red = int(split_5[1])
            elif split_5[2] == "green":
                green = int(split_5[1])
            elif split_5[2] == "blue":
                blue = int(split_5[1])

        game.add_subset(red, green, blue)

    games.append(game)

sum = 0
for game in games:
    if game.is_valid():
        sum += game.index

print("1 - ", sum)

sum = 0
for game in games:
    sum += game.power()

print("2 - ", sum)

