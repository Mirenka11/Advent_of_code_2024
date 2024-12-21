import pandas as pd 
data = pd.read_csv("input_data.txt", header=None, sep="   ", engine="python")
sorted_data = list(zip(sorted(data[0]), sorted(data[1])))
print(sorted_data)
cumulative_distance = 0
#print(data)
for i, j in sorted_data:
    cumulative_distance += abs(i-j)

print(cumulative_distance)
