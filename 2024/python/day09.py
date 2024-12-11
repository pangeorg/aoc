import utils

def solve1():
    line = utils.read_lines("../input/day09.txt")[0]
    values = [int(c) for c in line]
    expanded = []
    i = 0
    pid = 0
    while i < len(values) - 2:
        block = values[i] * [pid]
        expanded.extend(block)
        free = values[i+1] * ['.']
        expanded.extend(free)
        pid += 1
        i += 2
    expanded.extend(values[-1] * [pid])

    p1, p2 = 0, len(expanded) - 1

    while p1 < p2:
        if expanded[p1] == '.':
            expanded[p1] = expanded[p2]
            expanded[p2] = '.'
            p2 -= 1
        if expanded[p2] == '.':
            p2 -= 1
            continue
        p1 += 1

    result = 0
    for i, e in enumerate(expanded):
        if (e == '.'):
            break
        result += (i * e)
    print(result)

def solve2():
    line = utils.read_lines("../input/day09.txt")[0]
    values = [int(c) for c in line]
    pid = 0
    files = {}
    free = []
    pos = 0
    for i, file_size in enumerate(values):
        if i % 2 == 0:  # file
            files[pid] = (pos, file_size)
            pid += 1
        else:
            free.append((pos, file_size))
        pos += file_size

    # now we go backwards through ther files
    while pid > 0:
        pid = pid - 1
        pos, file_size = files[pid]
        for i, fr in enumerate(free):
            free_start, free_len = fr[0], fr[1]
            if free_start >= pos:
                free = free[:i]
                break
            if file_size <= free_len:
                files[pid] = (free_start, file_size)
                if free_len == file_size:
                    free.pop(i)
                else:
                    free[i] = (free_start + file_size, free_len - file_size)
                break
    result = 0
    for k, file_size in files.items():
        for i in range(file_size[0], file_size[0] + file_size[1]):
            result += k * i
    print(result)


solve2()
