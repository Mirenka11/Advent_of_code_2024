import re 

def mul(a:int, b:int)-> int:
    return a*b

with open("Day_03/input_data.txt", "r") as input_data:
    corrupted_data = input_data.read()
    corrupted_data = corrupted_data.replace("\n", "")
instructions = re.sub(r"do\(\)", "\ndo()", corrupted_data)
instructions = re.sub(r"don't\(\)", "\ndon't()", instructions)

instructions = instructions.split("\n")


instructions_do = []
instructions_dont = [] #kontrolni soucet
for instruction in instructions:
    print(instruction, end = "\n\n")
    if re.findall(r"^don't\(\)", instruction):
        instructions_dont += re.findall(r"mul\(\d{1,3},\d{1,3}\)", instruction)
    else:
        instructions_do += re.findall(r"mul\(\d{1,3},\d{1,3}\)", instruction)
added_results_do = 0
added_results_dont = 0
for instruction in instructions_do:
    added_results_do += eval(instruction)
for instruction in instructions_dont:
    added_results_dont += eval(instruction)

print(f"do: {added_results_do}\n\
don't: {added_results_dont}\n\
sum: {added_results_dont+added_results_do}\n\
check_sum: {170068701 - (added_results_dont+added_results_do)}")

