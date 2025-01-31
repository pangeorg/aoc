module Utils

module Grid = 

    // Grid relates stuff
    type Direction =
        | N
        | S
        | E
        | W

    let arrayToDirection arrow =
        match arrow with
        | '^' -> N
        | 'v' -> S
        | '>' -> E
        | '<' -> W
        | _ -> failwith ("Unknown instruction " + string arrow)

    let everyNth n seq =
        seq
        |> Seq.mapi (fun i el -> el, i) // Add index to element
        |> Seq.filter (fun (_, i) -> i % n = 0) // Take every nth element
        |> Seq.map fst // Drop index from the result

    let move (pos: int * int) (dir: Direction) =
        match dir with
        | N -> (fst pos), (snd pos) - 1
        | S -> (fst pos), (snd pos) + 1
        | E -> (fst pos + 1), (snd pos)
        | W -> (fst pos - 1), (snd pos)

    let neighbors (pos: int * int) =
        seq {
            for dir in [ N; S; E; W ] do
                yield move pos dir
        }

module String = 
    let inline intToChar i = char (i + int '0')

    let explodeStr (s: string) = [ for c in s -> c ]

    /// Converts a list of characters into a string.
    let implodeStr (xs: char list) =
        let sb = System.Text.StringBuilder(xs.Length)
        xs |> List.iter (sb.Append >> ignore)
        sb.ToString()

module Itertools = 
    let rec permute (list: 'a list) =
        match list with
        | [] -> [ [] ]
        | x :: xs -> List.collect (fun perm -> [ for i in 0 .. List.length perm -> List.insertAt i x perm ]) (permute xs)
    
module Graph = 
    open System
    open System.Collections.Generic
    open Itertools

    type DistanceGraph<'key> = Dictionary<'key, Dictionary<'key, int>>

    let calculateDistance (connections: DistanceGraph<'key>) (route: 'key list) =
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

    let findLongestRoute (connections: DistanceGraph<'key>) (locations: 'key list) =
        let routes = permute locations

        routes |> List.maxBy (calculateDistance connections)
        
    let addConnection (connections: DistanceGraph<'key>) (from: 'key) (to_: 'key) (distance: int) =
        if not (connections.ContainsKey(from)) then
            connections.[from] <- Dictionary<'key, int>()

        connections.[from].[to_] <- distance

        if not (connections.ContainsKey(to_)) then
            connections.[to_] <- Dictionary<'key, int>()

        connections.[to_].[from] <- distance
    