def normal_check(numbers):
    is_increasing = all(a <= b for a, b in zip(numbers, numbers[1:]))
    is_decreasing = all(a >= b for a, b in zip(numbers, numbers[1:]))
    is_sorted = is_increasing or is_decreasing
    
    differences = [abs(b - a) for a, b in zip(numbers, numbers[1:])]
    valid_differences = all(1 <= diff <= 3 for diff in differences)
    
    return is_sorted and valid_differences


def dampener_check(numbers):
    return any(normal_check(numbers[:i] + numbers[i+1:]) for i in range(len(numbers)))


valid_normal = valid_dampener = 0
with open('input/02.txt', 'r') as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        valid_normal += normal_check(numbers)
        valid_dampener += dampener_check(numbers)
        
# part1
print(valid_normal)

# part2
print(valid_dampener)