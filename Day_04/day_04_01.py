
def transpose(word_search:list[str])->list[str]:
    n_rows = len(word_search)
    
    transposed = ["" for i in range(len(word_search[0]))]
    for row_index in range(n_rows):
        for col_index in range(len(word_search[row_index])):
            transposed[col_index]+=word_search[row_index][col_index]
    return transposed

def read_diagonal(word_search:list[str], antidiagonal = False)->list[str]:
    n_rows = len(word_search)
    diagonal = ["" for i in range(n_rows+len(word_search[0]))]
    if antidiagonal:
        for row_index in range(n_rows):
            n_cols = len(word_search[row_index])
            for col_index in range(n_cols):
                diagonal[row_index+col_index]+=word_search[row_index][col_index]
    else:
        for row_index in range(n_rows):
            n_cols = len(word_search[row_index])
            for col_index in range(n_cols):
                diagonal[row_index-col_index+n_rows-1]+=word_search[row_index][col_index]
    return diagonal


with open("Day_04/input_data.txt", "r") as input_data:
    word_search = tuple(input_data.readlines())

xmas_found = 0
for line in word_search:
    xmas_found += line.count("XMAS")
    xmas_found += line.count("SAMX")

transposed = transpose(list(word_search))
for line in transposed:
    xmas_found += line.count("XMAS")
    xmas_found += line.count("SAMX")

diagonal = read_diagonal(list(word_search))
for line in diagonal:
    xmas_found += line.count("XMAS")
    xmas_found += line.count("SAMX")

antidiagonal = read_diagonal(list(word_search), antidiagonal=True)
for line in antidiagonal:
    xmas_found += line.count("XMAS")
    xmas_found += line.count("SAMX")

print(xmas_found)

