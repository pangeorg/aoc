module Day04

open System.Security.Cryptography
open System.Text
open System

let input = "bgvyzdsv"

let md5 (data: byte array) : string =
    use md5 = MD5.Create()

    (StringBuilder(), md5.ComputeHash(data))
    ||> Array.fold (fun sb b -> sb.Append(b.ToString("x2")))
    |> string

let getHash (num: int) =
    md5 (Encoding.ASCII.GetBytes(input + Convert.ToString num))


let part1 () =
    let num = 100000
    let hashes = seq { for i in num .. num * 10000 -> getHash i }
    let b = hashes |> Seq.findIndex (fun h -> h.StartsWith "000000")
    printfn "%d" (b + num)
    printfn "%s" (getHash (b + num))

let part2 () = ()
