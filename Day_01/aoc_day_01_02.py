import pandas as pd 
data = pd.read_csv("input_data.txt", header=None, sep="   ", engine="python")

reference = set(data[0])
data[1]
similarity_score = 0

for number in data[1]:
    if number in reference:
        similarity_score += number
		
print(similarity_score)