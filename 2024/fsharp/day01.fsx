open System.IO;
open System;

let lines = File.ReadAllLines("../input/day01.txt")

let part1 (lines: string array) = 
    let aToTuple (x: array<int>) = x[0], x[1]

    let left, right = 
        lines |> 
        Array.map (fun x -> (x.Split(" ") |> Array.map int) |> aToTuple) |>
        Array.unzip |> fun x -> (fst x, snd x)

    let lefts = Array.sort left
    let rights = Array.sort right
    let result = Array.map2 (fun l r -> Math.Abs((int)r - l)) lefts rights |> Array.sum

    printf "%A" result

let part2 (lines: string array) = 
    let aToTuple (x: array<int>) = x[0], x[1]
    let left, right = 
        lines |> 
        Array.map (fun x -> (x.Split(" ") |> Array.map int) |> aToTuple) |>
        Array.unzip
    
    let counts = Array.countBy (fun x -> x) right |> Map.ofArray

    let getCount (x: int) = 
        match counts.TryFind x with
        | Some v -> v
        | None -> 0

    let result = Array.map2 (fun l r -> l * getCount l) left right |> Array.sum
    printfn "%A" result
        
part2 lines