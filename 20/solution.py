import math
import queue  

with open('input', 'r') as fp:
    data = fp.read()

data = data.split("\n")

puzzle = {}
for configuration in data:
    source, destinations = configuration.split(" -> ")
    if source == "broadcaster":
        source_type = source
        source_name = source
        data = None
    else:
        source_type = source[0]
        source_name = source[1:]
        if source_type == "%":
            data = "off"
        else:
            data = {}

    puzzle[source_name] = [source_type, data, destinations.split(", ")]

for source in list(puzzle):
    source_type, data, destinations = puzzle[source]
    for destination in destinations:
        if destination not in puzzle:
            puzzle[destination] = [destination, None, []]
        
        if puzzle[destination][0] == "&":
            puzzle[destination][1][source] = "low"

signals = []
mmc = {}
for i in range(1, 1000000):
    q = queue.Queue()
    q.put(["button", "broadcaster", "low"])
    while not q.empty():       
        action_source, action_destination, action_signal = q.get()
        
        if i <= 1000:
            signals.append(action_signal)
        if action_destination == "ft" and action_signal == "high":
            if action_source not in mmc:
                mmc[action_source] = i

        # print("{} -{}-> {}".format(action_source, action_signal, action_destination))

        communication = puzzle[action_destination]
        if communication[0] == "broadcaster":
            for destination in communication[2]:
                q.put([action_destination, destination, action_signal])
        elif communication[0] == "%":
            if action_signal  == "high":
                continue
            if puzzle[action_destination][1] == "off":
                puzzle[action_destination][1] = "on"
                new_signal = "high"
            else:
                puzzle[action_destination][1] = "off"
                new_signal = "low"
            
            for destination in communication[2]:                   
                q.put([action_destination, destination, new_signal])
        elif communication[0] == "&":
            if len(puzzle[action_destination][1].values()) == 1:
                if action_signal == "low":
                    new_signal = "high"
                else:
                    new_signal = "low"

                for destination in communication[2]:                   
                    q.put([action_destination, destination, new_signal])
            else:
                puzzle[action_destination][1][action_source] = action_signal
                if list(puzzle[action_destination][1].values()).count("high") == len(puzzle[action_destination][1].values()):
                    new_signal = "low"
                else:
                    new_signal = "high"
                for destination in communication[2]:
                    q.put([action_destination, destination, new_signal])
    if len(mmc) == 4:
        break

print("Sum 1", signals.count("high") * signals.count("low"))
print("Sum 2", math.lcm(*list(mmc.values())))
