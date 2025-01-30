#r "System"
#load "Utils.fs"

open System.Collections.Generic
open System

let input = "1321131112" |> Seq.toList |> Seq.map (fun x -> Int32.Parse(x.ToString())) |> Seq.toList

// 'ugly' python reimplementation
let lookAndSay (input: int list) (times: int) =
    let findNext (input: int array) (currentIndex: int) =
        if input.Length = 1 then
            1
        else
            let mutable i = currentIndex
            let mutable value = input.[i]
            while i < input.Length && value = input.[i] do
                i <- i + 1
            i
    match input with
    | [] -> [] |> Seq.toArray
    | xs -> 
        let mutable result = [for x in xs -> x] |> Seq.toArray
        for n in 1 .. times do
            let mutable newResult = List<int>()
            let mutable i = 0
            while i < result.Length do
                let count = findNext result i
                newResult.Add(count)
                newResult.Add(result.[i])
                i <- count
            result <- newResult |> Seq.toArray
            printf "%d:%A\n" n result.Length
        result

(* F#-y way of solving it: http://theburningmonk.com/2015/12/advent-of-code-f-day-10/ *)
let read (input : string) =
    input
    |> Seq.fold (fun acc x ->
        match acc with
        | (n, x')::tl when x = x' -> (n+1, x')::tl
        | _ -> (1, x)::acc) []
    |> List.rev
    |> Seq.collect (fun (n, x) -> sprintf "%d%c" n x)
    |> fun xs -> System.String.Join("", xs)       

let genseqf (s : string) n =
    let res = 
        { 1..n }
        |> Seq.fold (fun last _ -> read last) s
        |> Seq.length

    res

let r = genseqf "1" 40
printf "%d" r
