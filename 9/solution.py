with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

def generate_next_sequence(sequence) -> list[int]:
    ret = []
    for i in range(len(sequence)):
        if i + 1 >= len(sequence):
            break
        a, b = sequence[i], sequence[i + 1]
        ret.append(b - a)

    return ret

count = 0
for history in data:
    history = list(map(int, history.split()))
    sequences = []
    sequences.append(history)
    next_sequence = history
    while True:
        next_sequence = generate_next_sequence(next_sequence)
        sequences.append(next_sequence)

        if len(set(next_sequence)) == 1 and next_sequence[0] == 0:
            break
    
    for i, sequence in reversed(list(enumerate(sequences))):
        if i + 1 == len(sequences):
            sequence.append(0)
        else:
            sequence.append(sequences[i + 1][-1] + sequence[-1])

    count += sequences[0][-1]

print("Sum 1", count)

count = 0
for history in data:
    history = list(map(int, history.split()))
    sequences = []
    sequences.append(history)
    next_sequence = history
    while True:
        next_sequence = generate_next_sequence(next_sequence)
        sequences.append(next_sequence)

        if len(set(next_sequence)) == 1 and next_sequence[0] == 0:
            break
    
    for i, sequence in reversed(list(enumerate(sequences))):
        if i + 1 == len(sequences):
            sequence.insert(0,0)
        else:
            sequence.insert(0,sequence[0] - sequences[i + 1][0])

    count += sequences[0][0]

print("Sum 2", count)