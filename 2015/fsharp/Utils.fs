module Utils

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

let explodeStr (s: string) = [ for c in s -> c ]

/// Converts a list of characters into a string.
let implodeStr (xs: char list) =
    let sb = System.Text.StringBuilder(xs.Length)
    xs |> List.iter (sb.Append >> ignore)
    sb.ToString()
