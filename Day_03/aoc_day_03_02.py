import re 
def mul(a:int, b:int)-> int:
    return a*b

with open("Day_03/input_data.txt", "r") as input_data:
    corrupted_data = input_data.read()
#corrupted_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
do = re.sub(r"don't\(\).*do\(\)", "do()", corrupted_data)
  
print(do)
#print(len(corrupted_data)-len(do))
print(re.findall("don't", do))

instructions_do = re.findall("mul\([0-9]+,[0-9]+\)", do)
#print(instructions_do)


added_results = 0
for instruction in instructions_do:
    added_results += eval(instruction)
print(added_results)

