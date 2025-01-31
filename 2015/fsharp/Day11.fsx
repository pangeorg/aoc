#r "System"

open System

let charToValue (c: char) = int c - int 'a' + 1

let valueToChar (value: int) =
    if value <= 0 then failwith "Value must be positive"
    else
        let rec loop v acc =
            if v <= 26 then (char (int 'a' + v - 1)) :: acc
            else loop ((v - 1) / 26) ((char (int 'a' + (v - 1) % 26)) :: acc)
        loop value [] |> List.rev |> System.String.Concat

let stringToValue (s: string) =
    s |> Seq.fold (fun acc c -> acc * 26 + charToValue c) 0

let valueToString (value: int) =
    valueToChar value

let addAlphabetStrings (a: string) (b: string) =
    let sum = stringToValue a + stringToValue b
    valueToString sum

let t = addAlphabetStrings "aaa" "bbb"
printf "%A" t
    