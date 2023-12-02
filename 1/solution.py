class Digit:
    position = 0
    digit = '0'
    spelled = False

    def __init__(self, position, digit, spelled):
        self.position = position
        self.digit = digit
        self.spelled = spelled

    def __str__(self) -> str:
        return "{} {} {}".format(self.position, self.digit, self.spelled)
    

with open('input', 'r') as fp:
    data = fp.readlines()

keywords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum_1 = 0
sum_2 = 0
for line in data:
    digits_1 = []
    digits_2 = []
    for i in range(len(keywords)):
        keyword = keywords[i]
        j = line.find(keyword)
        while j != -1:
            digits_2.append(Digit(j, i + 1, True))
            j = line.find(keyword, j + 1)


    for i in range(len(line)):
        digit = line[i]
        if digit.isnumeric():
            digits_1.append(Digit(i, digit, False))
            digits_2.append(Digit(i, digit, False))

    digits_2.sort(key=lambda x: x.position)

    cal_val = '{}{}'.format(digits_1[0].digit,digits_1[-1].digit)
    sum_1 += int(cal_val)
    cal_val = '{}{}'.format(digits_2[0].digit,digits_2[-1].digit)
    sum_2 += int(cal_val)

print("1", sum_1)
print("2", sum_2)
