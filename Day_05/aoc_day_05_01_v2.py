from functools import cmp_to_key
# splneno s pomoci
# TODO: zkusit to prepsat jinak

with open('Day_05/input_data.txt') as input_data:
    rules, pages = input_data.read().split('\n\n')

cmp = cmp_to_key(lambda lower, higher: -(lower+'|'+higher in rules)) # tohle je silena cerna magie
 
sum_middle_pages = 0
for page_sequence in pages.split():
    page_list = page_sequence.split(',')
    sorted_pages = sorted(page_list, key=cmp)
    if page_list == sorted_pages:
        sum_middle_pages += int(sorted_pages[len(sorted_pages)//2])

print(sum_middle_pages)


    
