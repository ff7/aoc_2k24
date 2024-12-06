def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    
    directions = [
        (-1, -1), 
        (-1, 0), 
        (-1, 1),
        (0, -1),           
        (0, 1),
        (1, -1),  
        (1, 0),  
        (1, 1)    
    ]
    
    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def check_direction(start_row, start_col, direction):
        row_delta, col_delta = direction
        current_word = ""
        
        row, col = start_row, start_col        
        for _ in range(len(word)):
            if not is_valid_position(row, col):
                return False
            current_word += matrix[row][col]
            row += row_delta
            col += col_delta
            
        return current_word == word
    
    for row in range(rows):
        for col in range(cols):
            for direction in directions:
                count += check_direction(row, col, direction)
    
    return count

def find_submatrices(matrix, patterns):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    all_matches = 0
    
    def check_pattern(start_row, start_col, pattern):
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])
        
        if start_row + pattern_rows > matrix_rows or start_col + pattern_cols > matrix_cols:
            return False
            
        for i in range(pattern_rows):
            for j in range(pattern_cols):
                pattern_char = pattern[i][j]
                matrix_char = matrix[start_row + i][start_col + j]
                
                if pattern_char != '*' and pattern_char != matrix_char:
                    return False
        return True
    
    for pattern_idx, pattern in enumerate(patterns):
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])
        
        if pattern_rows > matrix_rows or pattern_cols > matrix_cols:
            all_matches[pattern_idx] = []
            continue
            
        for row in range(matrix_rows - pattern_rows + 1):
            for col in range(matrix_cols - pattern_cols + 1):
                if check_pattern(row, col, pattern):
                    all_matches += 1
    
    return all_matches

with open('input/04.txt', 'r') as file:
    matrix = [line.strip() for line in file.readlines()]

    # part1
    word = "XMAS"
    print(find_word(matrix, word))

    # part2 -- quite hacky but didnt enjoy this one
    patterns = [
    [
        ["M", "*", "S"],
        ["*", "A", "*"],
        ["M", "*", "S"]
    ],
    [
        ["M", "*", "M"],
        ["*", "A", "*"],
        ["S", "*", "S"]
    ],
    [
        ["S", "*", "S"],
        ["*", "A", "*"],
        ["M", "*", "M"]
    ],
    [
        ["S", "*", "M"],
        ["*", "A", "*"],
        ["S", "*", "M"]
    ]
]
    print(find_submatrices(matrix, patterns))