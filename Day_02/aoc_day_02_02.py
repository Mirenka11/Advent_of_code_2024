def something_like_derivative(report:list[int])->list[int]:
    """Calculates difference between each adjacent levels in a report.

    Args:
        report (list[int]): list containing numbers called "levels"

    Returns:
        list[int]: distances between levels
    """
    it_1 = iter(report)
    it_2 = iter(report)
    next(it_2)
    slope = []
    for level in it_2:
        slope.append(level - next(it_1))
    return slope
                 
def is_safe(data:list[int], slope_provided = False)->bool:
    """Decide whether report is safe. The report contains numbers called "levels".
     A report only counts as safe if both of the following are true:

        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.

    Args:
        report (list[int]): derivative of levels

    Returns:
        bool: True if report is safe (according to the description above)
    """
    if not slope_provided:
        slope = something_like_derivative(data)
    else: slope = data
    if all(difference > 0 and difference <= 3 for difference in slope):
        return True
    elif all(difference < 0 and difference >= -3 for difference in slope):
        return True
    else: return False

def problem_dampener(report:list[int])->bool:
    """Assigns report as safe if one value can be removed

    Args:
        report (list[int]): list containing numbers called "levels"
        side (str): left or right
    Returns:
        bool: True if report with one datapoint removed is safe
    """
    if is_safe(report):
        return True
    if is_safe(report[1:]): # overim jestli to nezachrani odstraneni hodnoty na zacatku nebo na konci
        return True 
    if is_safe(report[:-1]):
        return True

    slope = something_like_derivative(report)
    
    positive_values = len(list(filter(lambda diff: diff > 0, slope)))
    negative_values = len(list(filter(lambda diff: diff < 0, slope)))
    enum_slope = list(enumerate(slope))
    if positive_values > negative_values:
        bad_values = list(filter(lambda diff: (diff[1] <= 0 or diff[1] > 3), enum_slope))
    else: 
        bad_values = list(filter(lambda diff: (diff[1] >= 0 or diff[1] < 3), enum_slope))
    
    for index, _ in bad_values:
        if index != 0 and index!= len(slope)-1: # tohle uz jsem checkovala
            polished_data = slope[0:index] + [slope[index-1] + slope[index]] + slope[index+1:]
            if is_safe(polished_data, slope_provided=True):
                return True
        if index <= len(slope)-2: # tohle taky
            polished_data = slope[0:index] + [slope[index+1] + slope[index]] + slope[index+2:]
            if is_safe(polished_data, slope_provided=True):
                return True
    return False
           

with open("Day_02/input_data.txt", "r") as input_data:
    data = [line.strip() for line in input_data.readlines()]
    data = [[int(n) for n in line.split()] for line in data] # tohle je strasna abomination ale funguje to

safe_reports = 0
for line in data:
    if problem_dampener(line): 
        safe_reports += problem_dampener(line)

print(safe_reports)