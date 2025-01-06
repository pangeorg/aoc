module Day01

open System
open System.IO

let private count1 (span: ReadOnlySpan<char>) =
    let mutable left, right = 0, 0

    for c in span do
        if c = ')' then right <- right + 1 else left <- left + 1

    left - right

let private count2 (str: string) =
    let rec countHelp (str: string) (floor: int) (index: int) =
        if index = (str.Length) then
            str.Length - 1
        else if floor = -1 then
            index - 1
        else if str.[index - 1] = ')' then
            countHelp str (floor - 1) (index + 1)
        else
            countHelp str (floor + 1) (index + 1)

    countHelp str 0 1


let part1 =
    let line = File.ReadAllLines("../input/day01.txt").[0]
    let chars = MemoryExtensions.AsSpan(line)
    let result = count1 chars
    printf "%d\n" result

let part2 =
    let line = File.ReadAllLines("../input/day01.txt").[0]
    let result = count2 line
    printf "%d\n" result
