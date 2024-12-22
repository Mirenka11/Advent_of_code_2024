# povolene tvary:
# M . S     S . S      M . S    S . M    M . M
# . A .     . A .      . A .    . A .    . A .
# M . S     M . M      M . S    S . M    S . S
# uprostred je vzdy "A"
# v rozich je vzdy 2*"M" a 2*"S", 
#   pricemz "M" a "S" jsou vzdy v protilehlych rozich

with open("Day_04/input_data.txt", "r") as input_data:
    word_search = tuple(input_data.readlines())

xmas_found = 0

n_rows = len(word_search)
for row_index in range(1, n_rows-1):
    n_cols = min([len(word_search[row_index]), 
                  len(word_search[row_index-1]), 
                  len(word_search[row_index+1])])
    for col_index in range(1, n_cols-1):
        if word_search[row_index][col_index] == "A":
            corners = [word_search[row_index-1][col_index-1], # levy horni roh         [0] . [1]  
                       word_search[row_index-1][col_index+1], # pravy horni roh            .
                       word_search[row_index+1][col_index-1], # levy dolni roh         [2] . [3]
                       word_search[row_index+1][col_index+1]] # pravy dolni roh
            if corners.count("M") == corners.count("S") == 2:
                if corners[0] != corners[3] and corners[1] != corners[2]:
                    xmas_found += 1

print(xmas_found)




