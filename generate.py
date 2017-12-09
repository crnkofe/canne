import sys
import random

class Competitor(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __str__(self):
        return self.name

competitors = []
competitors_file = sys.argv[1]
with open(competitors_file) as f:
    for line in f:
        split_line = tuple(line.split())
        name, sex = " ".join(split_line[:len(split_line) - 1]), split_line[-1]
        competitors.append(Competitor(name, sex))

pools = int(sys.argv[2])
if pools < 1:
    print("Cannot have less than 1 pool")
    sys.exit(1)
if pools > len(competitors):
    print("Cannot have more pools than competitors")
    sys.exit(1)

def humane_pool(pool_competitors):
    # assign random numbers to each competitor
    numbered_competitors = [x + 1 for x in range(len(pool_competitors))]

    pairs = []
    for idx, yellow in enumerate(numbered_competitors):
        for blue in numbered_competitors[idx+1:]:
            pairs.append((yellow, blue))

    # permutate pairs so competitor doesn't have two fights in a row
    humane_pairs = []
    previous = (0, 0)
    while len(pairs) != 0:
        frequencies = {}
        for x, y in humane_pairs:
            frequencies[x] = frequencies.get(x, 0) + 1
            frequencies[y] = frequencies.get(y, 0) + 1

        current_frequency_sum = frequencies.get(pairs[0][0], 0) + frequencies.get(pairs[0][1], 0)
        least_frequent = pairs[0]
        for pair in pairs:
            frequency_sum = frequencies.get(pair[0], 0) + frequencies.get(pair[1], 0)
            was_previous = (pair[0] in previous or pair[1] in previous)
            if frequency_sum < current_frequency_sum and not was_previous:
                current_frequency_sum = frequency_sum
                least_frequent = pair

        humane_pairs.append(least_frequent)
        pairs.remove(least_frequent)
        previous = humane_pairs[-1]
    return humane_pairs

shuffled_competitors = random.shuffle(competitors)
pool_length = len(competitors) / pools
for pool in range(pools):
    start_pool = pool * pool_length
    print("Pool {}".format(pool + 1))
    pool_competitors = competitors[start_pool:start_pool+pool_length]
    for idx, pair in enumerate(humane_pool(pool_competitors)):
        print("{}. {} : {}".format(idx + 1, pool_competitors[pair[0] -1], pool_competitors[pair[1]-1]))
