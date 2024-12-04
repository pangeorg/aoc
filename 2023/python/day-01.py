
literal_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
literal_numbers_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_calibration_1(s: str):
    n = len(s)
    first_found = False
    last_found = False
    result = 0

    for i in range(n):
        first = s[i]
        last = s[n - i - 1]
        if (not first_found) and first.isdigit():
            first_found = True
            result += 10 * int(first)
        if (not last_found) and last.isdigit():
            last_found = True
            result += int(last)
    return result

def find_calibration_2(s: str):
    n = len(s)
    first_found = False
    last_found = False
    result = 0

    def check_literal_forward(s, i) -> int:
        for n in range(len(literal_numbers)):
            lit = literal_numbers[n]
            sl = s[i:i+len(lit)]
            if sl == lit:
                return literal_numbers_values[n]
        return 0

    def check_literal_backwards(s, i) -> int:
        for n in range(len(literal_numbers)):
            lit = literal_numbers[n]
            sl = s[i - len(lit):i]
            if sl == lit:
                return literal_numbers_values[n]
        return 0
        
    for i in range(n):
        first = s[i]
        last = s[n - i - 1]
        forward = check_literal_forward(s, i)
        backward = check_literal_backwards(s, n - i)
        if (not first_found) and (first.isdigit() or forward):
            first_found = True
            if forward:
                result += 10 * forward
            else:
                result += 10 * int(first)
        if (not last_found) and (last.isdigit() or backward):
            last_found = True
            if backward:
                result += backward
            else:
                result += int(last)
    return result


with open("../data/day-01.txt", "r") as f:
    lines = f.readlines()

total = 0
for s in lines:
    calib = find_calibration_1(s)
    total += calib
print("Calibration 1: ", total)

total = 0
for s in lines:
    calib = find_calibration_2(s)
    total += calib
print("Calibration 2: ", total)
