
with open("../input/day14.txt") as f:
    lines = f.readlines()


lines = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
]
 

def parseLine(line): 
    split = line.strip().split()
    who = split[0]
    speed = int(split[3])
    duration = int(split[6])
    rest = int(split[-2])
    return who, speed, duration, rest

def getDist(time, speed, duration, rest):
    interval, remainder = divmod(time, duration + rest)
    return interval * speed * duration + speed * min(duration, remainder)
    
def getInfo(lines):
    result = {}
    for line in lines:
        who, speed, duration, rest = parseLine(line)
        result[who] = (speed, duration, rest)
    return result

def part1():

    time = 2503
    results = {}

    for line in lines:
        who, speed, duration, rest = parseLine(line)
        dist = getDist(time, speed, duration, rest)
        results[who] = dist

    print(list(sorted([(v, k) for k, v in results.items()]))[::-1])

def part2():

    time = 2503
    time = 1000
    
    info = getInfo(lines)
    points = {k: -1 for k in info.keys()}

    for i in range(time):
        results = {}
        for k in info.keys():
            speed, duration, rest = info[k]
            dist = getDist(i, speed, duration, rest)
            results[k] = dist
        winning = list(sorted([(v, k) for k, v in results.items()]))[::-1]
        _, winner = winning[0]
        points[winner] += 1
        
    print(list(sorted([(v, k) for k, v in points.items()]))[::-1])
    
part2()