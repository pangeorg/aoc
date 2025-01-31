from typing import List

input = [int(c) for c in "1321131112"]

def lookAndSay(input: List[int], n: int) -> List[int]:
    if len(input) == 0:
        return []

    def findNext(currentIndex: int, input: List[int]) -> int:
        inputLen = len(input)

        if inputLen == 1:
            return 1

        i = currentIndex
        value = input[i]
        while (input[i] == value):
            i += 1
            if i == inputLen:
                break
        return i

    result = [i for i in input]
    for _ in range(n):
        newResult = []
        i = 0
        while i < len(result):
            v = result[i]
            next = findNext(i, result)
            newResult.extend([next - i, v])
            i = next
        result = newResult

    return result


print(len(lookAndSay(input, 50)))
