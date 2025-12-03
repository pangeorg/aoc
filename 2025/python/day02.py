example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def is_invalid_2(num: int):
    num_str = str(num)
    n = len(num_str)
    window_size = n // 2
    while window_size > 0:
        left = 0
        right = left + window_size
        pattern = num_str[left:right]
        invalid = True
        while right < n:
            left = right
            right = left + window_size
            if pattern != num_str[left:right]:
                invalid = False
        if invalid:
            return invalid
        window_size -= 1
    return False


def is_invalid_1(num: int):
    num_str = str(num)
    n = len(num_str)
    if n % 2 == 0:
        left, right = num_str[0 : n // 2], num_str[n // 2 :]
        return left == right
    else:
        return False


def part1():
    with open("../data/day02.txt", "r") as f:
        data = f.readline()
    total = 0
    for id_range in data.split(","):
        from_range, to_range = id_range.split("-")
        from_range, to_range = int(from_range), int(to_range)
        for i in range(from_range, to_range + 1):
            if is_invalid_1(i):
                total += i

    print(total)


def part2():
    with open("../data/day02.txt", "r") as f:
        data = f.readline()
    # data = example
    total = 0
    for id_range in data.split(","):
        from_range, to_range = id_range.split("-")
        from_range, to_range = int(from_range), int(to_range)
        for i in range(from_range, to_range + 1):
            if is_invalid_2(i):
                total += i

    print(total)


part2()
# print(is_invalid_2(999))
# print(is_invalid_2(11))
# print(is_invalid_2(22))
# print(is_invalid_2(123123))
