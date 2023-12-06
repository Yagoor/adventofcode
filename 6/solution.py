def get_result(times, distances):
    sum = 1
    for time, distance in zip(times, distances):
        val = 0
        for i in range(1, time + 1):
            duration = time - i
            speed = (i)
            if speed * duration > distance:
                val += 1

        sum *= val

    return sum

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

times = list(map(int, data[0].split(":")[1].split()))
distances = list(map(int, data[1].split(":")[1].split()))

sum = get_result(times, distances)
print("Sum 1", sum)

times = [int(''.join(data[0].split(":")[1].split()))]
distances = [int(''.join(data[1].split(":")[1].split()))]

sum = get_result(times, distances)
print("Sum 2", sum)
