with open("Day_04/input_data.txt", "r") as input_data:
    word_search = tuple(input_data.readlines())

xmas_found = 0

# povolene tvary:
# M . S     S . S      M . S    S . M    M . M
# . A .     . A .      . A .    . A .    . A .
# M . S     M . M      M . S    S . M    S . S