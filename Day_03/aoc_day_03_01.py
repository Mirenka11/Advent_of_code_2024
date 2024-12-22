import re 
def mul(a:int, b:int)-> int:
    return a*b

with open("Day_03/input_data.txt", "r") as input_data:
    corrupted_data = input_data.read()

instructions = re.findall("mul\([0-9]+,[0-9]+\)", corrupted_data)
print(instructions)

added_results = 0
for instruction in instructions:
    added_results += eval(instruction)
print(added_results)