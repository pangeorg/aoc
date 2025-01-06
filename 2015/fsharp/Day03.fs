module Day03

open System.IO
open FSharp.Collections

let rec followInstructions (instructions: char list) (pos: int * int) (hist: Set<int * int>) =
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

        let updated = hist.Add newPos

        followInstructions (xs) (newPos) (updated)

let everyNth n seq =
    seq
    |> Seq.mapi (fun i el -> el, i) // Add index to element
    |> Seq.filter (fun (el, i) -> i % n = 0) // Take every nth element
    |> Seq.map fst // Drop index from the result

let part1 () =
    let instructions = File.ReadAllText("../input/day03.txt").Trim() |> Seq.toList
    let hist = followInstructions instructions (0, 0) (Set [ (0, 0) ])
    printfn "%d" hist.Count

let part2 () =
    let instructions = File.ReadAllText("../input/day03.txt").Trim() |> Seq.toList
    let santaInstructions = Seq.toList (List.toSeq instructions |> everyNth 2)
    let roboInstructions = Seq.toList (List.toSeq instructions[1..] |> everyNth 2)
    let santa = followInstructions santaInstructions (0, 0) (Set [ (0, 0) ])
    let robo = followInstructions roboInstructions (0, 0) (Set [ (0, 0) ])
    let common = Set.union santa robo
    printfn "%d" common.Count
