def is_safe(report:list[int])->bool:
    """Decide whether report is safe. The report contains numbers called "levels".
     A report only counts as safe if both of the following are true:

        - The levels are either all increasing or all decreasing.
        - Any two adjacent levels differ by at least one and at most three.

    Args:
        report (list[int]): list containing numbers called "levels"

    Returns:
        bool: True if report is safe (according to the description above)
    """

    it_1 = iter(report) # kdyz uz umim iteratory, tak je taky pouziju
    it_2 = iter(report)
    next(it_2) # posunu it_2 o jeden dopredu
    slope = next(it_2) - next(it_1)
    if slope == 0 or abs(slope) > 3:
        return False
    
    if slope > 0: # poradi je vzestupne
        for level in it_2:
            difference = level - next(it_1)
            if difference < 1 or difference > 3:
                return False
    elif slope < 0: # poradi je sestupne
        for level in it_2:
            difference = next(it_1) - level
            if difference < 1 or difference > 3:
                return False
          
    return True         



with open("Day_02/input_data.txt", "r") as input_data:
    data = [line.strip() for line in input_data.readlines()]
    data = [[int(n) for n in line.split()] for line in data] # tohle je strasna abomination ale funguje to

safe_reports = 0
for line in data:
    safe_reports += is_safe(line)

print(safe_reports)