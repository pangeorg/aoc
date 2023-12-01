def find_calibration(s: str):
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


total = 0
for s in ["1abc2", "qr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]:
    calib = find_calibration(s)
    total += calib
    print(s, calib, total)
