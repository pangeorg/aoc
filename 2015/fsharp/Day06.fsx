module Day06

open System
open System.IO

let input = File.ReadAllLines("../input/day06.txt")

type Command =
    | On
    | Off
    | Toggle
    
type Rectangle = {
    TopLeft: int * int
    BottomRight: int * int 
}

type Instruction = { 
    Command: Command
    Rectangle: Rectangle
}

let parseCoordinats (s: string) =
    s.Split "," |> Array.map Convert.ToInt32 |> Array.pairwise |> Array.exactlyOne


let parseLine (line: string) =
    let p = line.Split " "

    if p.[0] = "toggle" then
        { Instruction.Command = Toggle
          Instruction.Rectangle = 
            { TopLeft = parseCoordinats p.[1]
              BottomRight = parseCoordinats p.[3] }
        }
    else
        match p.[1] with
        | "on" ->
            { Instruction.Command = On
              Instruction.Rectangle = 
                { TopLeft = parseCoordinats p.[2]
                  BottomRight = parseCoordinats p.[4] }
            }
        | "off" ->
            { Instruction.Command = Off
              Instruction.Rectangle = 
                { TopLeft = parseCoordinats p.[2]
                  BottomRight = parseCoordinats p.[4] }
            }
        | _ -> failwith "Could not parse command"

let part1 () = 
    let grid = Array.init (1000 * 1000) (fun _ -> 0)
    let instructions = input |> Array.map parseLine
    for i in instructions do
        for x in fst i.Rectangle.TopLeft .. fst i.Rectangle.BottomRight do
            for y in snd i.Rectangle.TopLeft .. snd i.Rectangle.BottomRight do
                let index = y * 1000 + x
                match i.Command with
                | On -> grid.[index] <- 1
                | Off -> grid.[index] <- 0
                | Toggle -> match grid.[index] with
                            | 0 -> grid.[index] <- 1
                            | _ -> grid.[index] <- 0
    let result = Array.sum grid
    printfn "%A" result

let part2 () = 
    let grid = Array.init (1000 * 1000) (fun _ -> 0)
    let instructions = input |> Array.map parseLine
    for i in instructions do
        for x in fst i.Rectangle.TopLeft .. fst i.Rectangle.BottomRight do
            for y in snd i.Rectangle.TopLeft .. snd i.Rectangle.BottomRight do
                let index = y * 1000 + x
                match i.Command with
                | On -> grid.[index] <- grid.[index] + 1
                | Off -> grid.[index] <- Math.Max(grid.[index] - 1, 0)
                | Toggle -> grid.[index] <- grid.[index] + 2
    let result = Array.sum grid
    printfn "%A" result