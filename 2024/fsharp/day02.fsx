#load utils.fsx
open Utils
open System.IO;

let lines = File.ReadAllLines("../input/sample02.txt")
let levelsList = 
    lines |> 
    Array.map (fun x -> x.Split(" ") |> Array.map int)
    
let isSave (levels: int array) = 
    let mutable maxDiff = 0
    let mutable sign = 0
    levels
    |> Seq.pairwise
    |> Seq.iter (fun (x, y) -> 
        let diff = (x - y)
        if abs(diff) > abs(maxDiff) then maxDiff <- diff
        
    )
    maxDiff < 3

    
let r = isSave [|1; 2; 3; 4; 5; 6; 2; 8; 9; 10|]
printfn "%b" r
