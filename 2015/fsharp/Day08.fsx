#r "System.IO"

open System.IO

let lines = File.ReadAllLines("../input/day08.txt")

let rec decodedCountChars (chars: list<char>) (count: int) : int =
    match chars with
    | [] -> count + 2 // add surrounding
    | '\\' :: 'x' :: _ :: _ :: rest -> decodedCountChars rest (count + 5)
    | '"' :: rest -> decodedCountChars rest (count + 2)
    | '\\' :: rest -> decodedCountChars rest (count + 2)
    | _ :: xs -> decodedCountChars xs (count + 1)

let decodedCount (str: string) : int =
    let c = str |> Seq.toList
    decodedCountChars c 0

let rec escapedCountChars (chars: list<char>) (count: int) : int =
    match chars with
    | []
    | [ _ ] -> count
    | '\\' :: '"' :: rest -> escapedCountChars rest (count + 1)
    | '\\' :: '\\' :: rest -> escapedCountChars rest (count + 1)
    | '\\' :: 'x' :: _ :: _ :: rest -> escapedCountChars rest (count + 1)
    | _ :: xs -> escapedCountChars xs (count + 1)

let escapedCount (str: string) : int =
    let c = str |> Seq.toList
    escapedCountChars c[1 .. c.Length - 1] 0

let part1 () =
    let mem = Array.map String.length lines |> Array.sum
    let charCount = Array.map escapedCount lines |> Array.sum
    printfn "%d" (mem - charCount)

let part2 () =
    let mem = Array.map String.length lines |> Array.sum
    let charCount = Array.map decodedCount lines |> Array.sum
    printfn "%d" (charCount - mem)

part2 ()
