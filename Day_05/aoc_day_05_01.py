from functools import cmp_to_key
# ok bylo by fajn pochopit jak tenhle neat trik funguje
def comparing_function(lower:int, higher:int):
    if (lower, higher) in rules:
        return -1
    elif (higher, lower) in rules:
        return 0
    else: return 0
with open("Day_05/input_data.txt", "r") as input_data:
    rules, pages = input_data.read().split('\n\n')

rules = [(int(i), int(j)) for rule in rules.split() for i, j in rule.split("|")]
sum_middle_pages = 0
for page_sequence in pages.split():
    page_list = page_sequence.split(',')
    sorted_pages = sorted(page_list, key=cmp_to_key(comparing_function)) # FIXME: takhle ne :(
    if page_list == sorted_pages:
        sum_middle_pages += int(sorted_pages[len(sorted_pages)//2])

print(sum_middle_pages)