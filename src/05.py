from collections import defaultdict

def is_sequence_valid(sequence, rules):
    positions = {num: pos for pos, num in enumerate(sequence)}
    
    for key, values in rules.items():
        if key in positions:
            key_pos = positions[key]
            for value in values:
                if value in positions and positions[value] < key_pos:
                    return False
    return True

rules = defaultdict(list)
sequences = []
    
with open('input/05.txt', 'r') as file:
    for line in file:
        if line.strip() == '':
            break
        key, value = map(int, line.strip().split('|'))
        rules[key].append(value)
        
    for line in file:
        if line.strip():
            numbers = [int(num) for num in line.strip().split(',')]
            sequences.append(numbers)


rules = dict(rules)
valid_middle = []
invalid_middle = []

for sequence in sequences:
    if is_sequence_valid(sequence, rules):
        valid_middle.append(sequence[len(sequence) // 2])
    else:
        # could also do this with a topological sort if we modelled the rules as a graph
        ordered = sorted(sequence, key=lambda x: sum(1 for v in rules.get(x, []) if v in sequence))
        invalid_middle.append(ordered[len(ordered) // 2])


# part1
print(sum(valid_middle))

# part2
print(sum(invalid_middle))
