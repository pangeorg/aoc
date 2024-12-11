#load utils.fsx
open Utils
open System.IO;

let lines = File.ReadAllLines("../input/sample02.txt")
let levelsList = 
    lines |> 
    Array.map (fun x -> x.Split(" ") |> Array.map int)
    
let isSave (levels: int array) = 
    let z = Array.zip levels[..Array.length levels - 2] (levels[1..])
    let d = Array.map (fun x -> snd x - fst x) z
    let max = Array.max d

    
isSave [|1; 2; 3; 4; 5; 6; 2; 8; 9; 10|]