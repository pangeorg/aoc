#r "System.IO"

open System
open System.IO
open System.Collections.Generic

let trips = File.ReadAllLines("../input/day09.txt")

let parseTrip (trip: string) =
    let parts = trip.Split([| " to "; " = " |], StringSplitOptions.None)
    parts.[0], parts.[1], Int32.Parse(parts.[2])

let addConnection
    (connections: Dictionary<string, Dictionary<string, int>>)
    (start: string)
    (end_: string)
    (distance: int)
    =
    if not (connections.ContainsKey(start)) then
        connections.[start] <- Dictionary<string, int>()

    connections.[start].[end_] <- distance

    if not (connections.ContainsKey(end_)) then
        connections.[end_] <- Dictionary<string, int>()

    connections.[end_].[start] <- distance

let connections = Dictionary<string, Dictionary<string, int>>()
let locations = HashSet<string>()

for trip in trips do
    let start, end_, distance = parseTrip trip
    locations.Add start |> ignore
    locations.Add end_ |> ignore
    addConnection connections start end_ distance

let rec permute (list: 'a list) =
    match list with
    | [] -> [ [] ]
    | x :: xs -> List.collect (fun perm -> [ for i in 0 .. List.length perm -> List.insertAt i x perm ]) (permute xs)

// Print the connections
for kvp in connections do
    printfn "%s:" kvp.Key

    for innerKvp in kvp.Value do
        printfn "  %s -> %d" innerKvp.Key innerKvp.Value

let calculateDistance (connections: Dictionary<string, Dictionary<string, int>>) (route: string list) =
    let rec loop route acc =
        match route with
        | []
        | [ _ ] -> acc
        | x :: y :: xs ->
            let distance =
                if connections.ContainsKey(x) && connections.[x].ContainsKey(y) then
                    connections.[x].[y]
                else
                    Int32.MaxValue

            loop (y :: xs) (acc + distance)

    loop route 0

let findShortestRoute (connections: Dictionary<string, Dictionary<string, int>>) (locations: string list) =
    let routes = permute locations

    routes |> List.minBy (calculateDistance connections)

let findLongestRoute (connections: Dictionary<string, Dictionary<string, int>>) (locations: string list) =
    let routes = permute locations

    routes |> List.maxBy (calculateDistance connections)

let locationsList = locations |> Seq.toList

let r = findShortestRoute connections locationsList
printfn "%A" r
printfn "%d" (calculateDistance connections r)

let l = findLongestRoute connections locationsList
printfn "%A" l
printfn "%d" (calculateDistance connections l)
