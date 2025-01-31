#r "System"

open System.Text.RegularExpressions
open System.IO
open System
open System.Text.Json
open System.Text.Json.Nodes

let input = File.ReadAllText "../input/day12.txt"

let part1 () =
    let rx = Regex(@"[-]?\d+", RegexOptions.Compiled)

    let x =
        (rx.Matches input |> Seq.toList)
        |> Seq.map (fun x -> Int32.Parse(x.Value))
        |> Seq.sum

    printfn "%A" x


let value = JsonNode.Parse input

let rec compute (root: JsonNode) =
    match root.GetValueKind() with
    | JsonValueKind.Object ->
        let o = root.AsObject()
        let mutable a = 0
        let mutable hasRed = false

        for k in o do
            if k.Value.GetValueKind() = JsonValueKind.String && k.Value.GetValue() = "red" then
                hasRed <- true

        if hasRed then
            0
        else
            for k in o do
                a <- a + compute k.Value

            a
    | JsonValueKind.Number -> root.GetValue()
    | JsonValueKind.Array ->
        let array = root.AsArray()
        let mutable a = 0

        for k in array do
            a <- a + compute k

        a
    | _ -> 0

let r = compute value
printfn "%d" r
