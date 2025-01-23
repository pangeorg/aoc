module Day02

open System.IO

let private area (l: int) (w: int) (h: int) =
    let lw = l * w
    let wh = w * h
    let hl = h * l
    2 * lw + 2 * wh + 2 * hl + Array.min [| lw; wh; hl |]

let private areaRibbon (l: int) (w: int) (h: int) =
    let faces = [| l; w; h |] |> Array.sort
    let vol = l * w * h
    let ribbon = 2 * faces.[0] + 2 * faces.[1]
    vol + ribbon

let private parseLine (line: string) = line.Split('x') |> Array.map int

let part1 =
    let lines = File.ReadAllLines("../input/day02.txt")
    let data = lines |> Array.map parseLine
    let result = data |> Array.map (fun x -> area x.[0] x.[1] x.[2]) |> Array.sum
    printfn "%d" result

let part2 =
    let lines = File.ReadAllLines("../input/day02.txt")
    let data = lines |> Array.map parseLine
    let result = data |> Array.map (fun x -> areaRibbon x.[0] x.[1] x.[2]) |> Array.sum
    printfn "%d" result
