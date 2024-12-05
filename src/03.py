import re

with open('input/03.txt', 'r') as file:
    text = file.read()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# part1
unfiltered_mult = [int(match.group(1)) * int(match.group(2)) for match in re.finditer(mul_pattern, text)]
print(sum(unfiltered_mult))

# part2
all_matches = sorted(
    [(match.start(), 'mul', (int(match.group(1)), int(match.group(2)))) for match in re.finditer(mul_pattern, text)] +
    [(match.start(), 'do', None) for match in re.finditer(r"do\(\)", text)] +
    [(match.start(), 'dont', None) for match in re.finditer(r"don't\(\)", text)],
    key=lambda x: x[0]
)

filtered_mult = []
enabled = True

for pos, cmd, values in all_matches:
    if cmd == 'do':
        enabled = True
    elif cmd == 'dont':
        enabled = False
    elif cmd == 'mul' and enabled:
        num1, num2 = values
        filtered_mult.append(num1 * num2)

print(sum(filtered_mult))