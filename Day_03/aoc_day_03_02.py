import re 
def mul(a:int, b:int)-> int:
    return a*b

with open("Day_03/input_data.txt", "r") as input_data:
    corrupted_data = input_data.read()

instructions_do = re.findall("do\(\)*mul\([0-9]+,[0-9]+\)", corrupted_data) # tohle nefunguje :( 
instructions_dont = re.findall("don't\(\)*mul\([0-9]+,[0-9]+\)", corrupted_data)
print(instructions_do)
print(instructions_dont) 