#r "System"
#load "Utils.fs"

open System
open System.IO
open System.Collections.Generic
open Utils.Itertools

let input = File.ReadAllLines "../input/day13.txt"

type HappinessAffect = {
    Who: string
    To: string
    Amount: int
}


let parseLine (line: string) =
    let s = line.Split()
    let sign = match s.[2] with
                    | "gain" -> 1
                    | _ -> -1
    {
        Who = s.[0]
        To = s.[10][0 .. s.[10].Length - 2]
        Amount = sign * Int32.Parse s.[3]
    }
    
let connections = Dictionary<string*string, int>()
let people = HashSet<string>()

let parsedLines = input |> Array.map parseLine

for h in parsedLines do
    people.Add h.Who |> ignore
    people.Add h.To |> ignore
    connections.TryAdd((h.Who, h.To), (h.Amount)) |> ignore
    
let totalHappiness (connections: Dictionary<string*string, int>) (input: string list) = 
    let mutable happiness = 0
    for i in 0 .. input.Length - 2 do
        happiness <- happiness + connections.[(input.[i], input.[i + 1])]
        happiness <- happiness + connections.[(input.[i + 1], input.[i])]
    happiness <- happiness + connections.[(input.[0], input.[input.Length - 1])]
    happiness <- happiness + connections.[(input.[input.Length - 1], input.[0])]
    happiness

let peopleList = people |> Seq.toList
let allPermutations = permute peopleList

let r = allPermutations |> Seq.map (totalHappiness connections) |> Seq.max

printfn "%A" r
    
