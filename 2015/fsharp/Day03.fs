module Day03

open System.IO
open FSharp.Collections

let rec followInstructions (instructions: char list) (pos: int * int) (hist: Map<int * int, int>) =
    match instructions with
    | [] -> hist
    | x :: xs ->
        let newPos =
            match x with
            | '^' -> (fst pos), (snd pos) - 1
            | 'v' -> (fst pos), (snd pos) + 1
            | '>' -> (fst pos + 1), (snd pos)
            | '<' -> (fst pos - 1), (snd pos)
            | _ -> failwith ("Unknown instruction " + string x)

        let updated =
            if hist.ContainsKey newPos then
                hist.Add(newPos, hist.[newPos] + 1)
            else
                hist.Add(newPos, 1)

        followInstructions (xs) (newPos) (updated)

let part1 () =
    let instructions = File.ReadAllText("../input/day03.txt").Trim() |> Seq.toList
    let hist = followInstructions instructions (0, 0) (Map [ (0, 0), 1 ])
    printfn "%d" hist.Keys.Count
