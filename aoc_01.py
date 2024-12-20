import pandas as pd 
data = pd.read_csv("input_data.txt", header=None, sep=" ")
sorted_data = [sorted(data[0]), sorted(data[1])]
