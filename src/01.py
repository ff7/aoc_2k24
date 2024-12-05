col1 = []
col2 = []

with open('input/01.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.strip().split())
        col1.append(num1)
        col2.append(num2)

col1.sort()
col2.sort()

# part1
differences = [abs(a - b) for a, b in zip(col1, col2)]
print(sum(differences))

# part2
similarity_scores = [num * col2.count(num) for num in col1]
print(sum(similarity_scores))