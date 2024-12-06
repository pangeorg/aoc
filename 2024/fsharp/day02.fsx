#load utils.fsx
open Utils
open System.IO;

let lines = File.ReadAllLines("../input/sample02.txt")
let levelsList = 
    lines |> 
    Array.map (fun x -> x.Split(" ") |> Array.map int)
    
let isSave (levels: int array) = ()
    
printfn "%A" levelsList