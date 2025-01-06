#load utils.fsx
open Utils
open System.IO;

let lines = File.ReadAllLines("../input/day02.txt")
let levelsList = 
    lines |> 
    Array.map (fun x -> x.Split(" ") |> Array.map int)
    
let sgn a = 
    if a >= 0 then 1
    else -1
        
let isSave (levels: int array) = 
    let mutable sign = sgn(levels.[0] - levels.[1])
    levels
    |> Seq.pairwise
    |> Seq.map (fun (x, y) -> 
        let d = x - y
        abs(d) <= 3 && abs(d) >= 1 && sign = sgn(d)
    )
    |> Seq.reduce (fun a b -> a && b)

let isSaveDamped (levels: int array) = 
    if isSave levels then true
    else 
        [1..levels.Length - 1]
        |> List.map (fun i -> Array.toList(levels.[0..i - 1]) @ Array.toList(levels.[i + 1..]))
        |> List.map (fun x -> isSave (List.toArray x))
        |> Seq.reduce (fun a b -> a || b)
    
    
let part1 = 
    let total = 
        levelsList
        |> Array.filter isSave
        |> Array.length
    printfn "%i" total

let part2 = 
    let total = 
        levelsList
        |> Array.filter isSaveDamped
        |> Array.length
    // let total = 
    //     levelsList
    //     |> Array.map isSaveDamped

    printfn "%A" total
    
part2