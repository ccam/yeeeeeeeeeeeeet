def parse_file():
    matrix = []
    with open("./past.txt", 'r', encoding='utf-8') as file:
        for line in file:
            if line != "\n": # removes empty lines from list
                matrix.append(line.strip("\n").split (" "))
                # .strip() above removes newline character from corrdinate list
    
    # set 2,3 columns to int
    cols = {1: int, 2: int} #lists start at 0 in python. not 1. 
    for row in matrix:
       for col_index, new_type in cols.items():
           row[col_index] = new_type(row[col_index]) 

    find_asterisk_and_neighbors(matrix)


# BFS algo should be implemented here.
def find_asterisk_and_neighbors(matrix):
    #allowed_chars = set(('═','║','╔','╗','╚','╝','╠','╣','╦','╩'))
    allowed_chars = set('═║╔╗╚╝╠╣╦╩')
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == '*':
                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                letters = []
                for nx, ny in neighbors:
                    if 0 <= nx < len(row) and 0 <= ny < len(matrix) and matrix[ny][nx] not in allowed_chars and matrix[ny][nx] != '*':
                        letters.append(matrix[ny][nx])
                print(letters)
    return []

parse_file()
letters = find_asterisk_and_neighbors(matrix)
print(letters)

