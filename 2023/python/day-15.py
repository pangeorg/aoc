from utils import *

def hashf(chars: str):
    val = 0
    for c in chars:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

def solve_1(lines):
    line = lines[0]
    vals = [hashf(chars) for chars in line.split(",")]
    print(sum(vals))

def solve_2(lines):
    line = lines[0]
    # ech box has a list of (label, focallength) tuples
    boxes = [[] for _ in range(256)]
    for op in line.split(","):
        if "=" in op:
            label_str, focal = op.split("=")
            focal = int(focal)
            ibox = hashf(label_str)
            box = boxes[ibox]
            found = False
            for slot, label_focal in enumerate(box):
                box_label, _ = label_focal
                if box_label == label_str:
                    box[slot] = box_label, focal
                    found = True
                    break
            if not found:
                box.append((label_str, focal,))
        if "-" in op:
            label_str = op[:-1]
            ibox = hashf(label_str)
            box = boxes[ibox]
            box = boxes[ibox]
            for slot, label_focal in enumerate(box):
                box_label, _ = label_focal
                if box_label == label_str:
                    box.pop(slot)
                    break
    total = 0
    for ibox, box in enumerate(boxes):
        if not len(box):
            continue
        box_total = 0
        for slot, label_focal in enumerate(box):
            label, focal = label_focal
            # print(f"{label}: {ibox + 1} (Box {ibox}) * {slot + 1} * {focal}")
            box_total += ((slot + 1) * focal * (ibox + 1))
        total += box_total
    print(total)

DAY = 15
test = False
if test:
    filename = "../data/sample-{:02d}.txt".format(DAY)
else:
    filename = "../data/day-{:02d}.txt".format(DAY)

lines = read_lines(filename)
# solve_1(lines)
solve_2(lines)
