l = [2, 1, 3, 5, 3, 2]
#  [-2, -1, -3, 5, -3, 2]

def add_from_file():
    total = 0
    with open('freqs.txt', 'r') as f:
        for line in f:
            total += int(line.strip())
    return total

# print(add_from_file())

def freq_twice():
    curr_frequency = 0
    seen = set([curr_frequency])
    while True:
        # for num in nums:
        with open('freqs.txt', 'r') as f:
            for line in f:
                curr_frequency += int(line.strip())
                if curr_frequency in seen:
                    return curr_frequency
                seen.add(curr_frequency)

# print(freq_twice())


def get_checksum():
    twos, threes = 0, 0
    with open('box_ids.txt', 'r') as f:
        for box_id in f:
            char_frequencies = get_char_frequencies(box_id.strip())
            twos += char_frequencies[0]
            threes += char_frequencies[1]
    return twos * threes

def get_char_frequencies(box_id):
    freqs = {}
    twos, threes = 0, 0
    for char in box_id:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    for freq in freqs.values():
        if not threes or not twos:
            if freq == 2:
                twos = 1
            elif freq == 3:
                threes = 1
        elif threes and twos:
            return threes, twos
    # print(freqs)
    return twos, threes

# print(get_checksum())

# def differ_by_one_at_position(box_id):

a = 'hello'

def equal(f):
    print(a is f)

# equal('hello')
