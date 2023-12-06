# Used one hint

SEEDS = 0
SEED_TO_SOIL = 1
SOIL_TO_FERTILIZER = 2
FERTILIZER_TO_WATER = 3
WATER_TO_LIGHT = 4
LIGHT_TO_TEMPERATURE = 5
TEMPERATURE_TO_HUMIDITY = 6
HUMIDITY_TO_LOCATION = 7

with open('input', 'r') as fp:
    data = fp.read()

maps = data.split("\n\n")

def merge_ranges(seeds, mappings):
    outputs = []

    for start, length in seeds:
        while length > 0:
            for mapping in mappings:
                destination, source, mapping_length = map(int, mapping.split())
                if source <= start < source + mapping_length:
                    mapping_length -= max(start - source, mapping_length - length)
                    outputs.append((start - source + destination, mapping_length))
                    start += mapping_length
                    length -= mapping_length
                    break
            else:
                outputs.append((start, length))
                break

    return outputs

seeds = list(map(int, maps[SEEDS].split(" ")[1:]))
seeds = list(zip(seeds, [1] * len(seeds)))
seeds = merge_ranges(seeds, maps[SEED_TO_SOIL].split("\n")[1:])
seeds = merge_ranges(seeds, maps[SOIL_TO_FERTILIZER].split("\n")[1:])
seeds = merge_ranges(seeds, maps[FERTILIZER_TO_WATER].split("\n")[1:])
seeds = merge_ranges(seeds, maps[WATER_TO_LIGHT].split("\n")[1:])
seeds = merge_ranges(seeds, maps[LIGHT_TO_TEMPERATURE].split("\n")[1:])
seeds = merge_ranges(seeds, maps[TEMPERATURE_TO_HUMIDITY].split("\n")[1:])
seeds = merge_ranges(seeds, maps[HUMIDITY_TO_LOCATION].split("\n")[1:])
print("Result 1", min(seeds)[0])

seeds = list(map(int, maps[SEEDS].split(" ")[1:]))
seeds = list(zip(seeds[0::2], seeds[1::2]))
seeds = merge_ranges(seeds, maps[SEED_TO_SOIL].split("\n")[1:])
seeds = merge_ranges(seeds, maps[SOIL_TO_FERTILIZER].split("\n")[1:])
seeds = merge_ranges(seeds, maps[FERTILIZER_TO_WATER].split("\n")[1:])
seeds = merge_ranges(seeds, maps[WATER_TO_LIGHT].split("\n")[1:])
seeds = merge_ranges(seeds, maps[LIGHT_TO_TEMPERATURE].split("\n")[1:])
seeds = merge_ranges(seeds, maps[TEMPERATURE_TO_HUMIDITY].split("\n")[1:])
seeds = merge_ranges(seeds, maps[HUMIDITY_TO_LOCATION].split("\n")[1:])
print("Result 2", min(seeds)[0])
