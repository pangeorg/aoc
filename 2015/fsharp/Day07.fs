module Day07

open System
open System.IO

let input = File.ReadAllLines("../input/day07.txt")

type WireInstruction =
    { LeftOperand: string
      RightOperand: string
      Instr: string }

let parseInstructions (line: string) =
    let split = line.Split " -> " |> Array.toList
    let left = split.[0]
    let right = split.[1]
    let instr = left.Split " "

    let wireInstr =
        if instr.Length = 1 then
            { WireInstruction.LeftOperand = left
              RightOperand = ""
              Instr = "SET" }
        else if instr.Length = 2 then
            { WireInstruction.LeftOperand = instr.[1]
              RightOperand = ""
              Instr = instr.[0] }
        else
            { WireInstruction.LeftOperand = instr.[0]
              RightOperand = instr.[2]
              Instr = instr.[1] }

    wireInstr, right

let performInstruction (instr: string) (leftOperand: uint16) (rightOperand: uint16) =
    match instr with
    | "SET" -> leftOperand
    | "NOT" -> ~~~(leftOperand)
    | "AND" -> leftOperand &&& rightOperand
    | "OR" -> leftOperand ||| rightOperand
    | "RSHIFT" -> leftOperand >>> Convert.ToInt32 rightOperand
    | "LSHIFT" -> leftOperand <<< Convert.ToInt32 rightOperand
    | _ -> failwith "Unknown instruction"

let rec calculate
    (wires: Collections.Generic.Dictionary<string, WireInstruction>)
    (results: Collections.Generic.Dictionary<string, uint16>)
    (wire: string)
    =
    if results.ContainsKey(wire) then
        results.[wire]
    else
        let wireInstr = wires.[wire]

        match wireInstr.Instr with
        | "SET" ->
            let r =
                match UInt16.TryParse(wireInstr.LeftOperand) with
                | true, x -> x
                | false, _ -> calculate wires results wireInstr.LeftOperand

            results.Add(wire, r)
            r
        | "NOT" ->
            let r =
                match UInt16.TryParse(wireInstr.LeftOperand) with
                | true, x -> ~~~x
                | false, _ -> ~~~(calculate wires results wireInstr.LeftOperand)

            results.Add(wire, r)
            r
        | inst ->
            let left =
                match UInt16.TryParse(wireInstr.LeftOperand) with
                | true, x -> x
                | false, _ -> calculate wires results wireInstr.LeftOperand

            let right =
                match UInt16.TryParse(wireInstr.RightOperand) with
                | true, x -> x
                | false, _ -> calculate wires results wireInstr.RightOperand

            results.Add(wire, performInstruction inst left right)
            results.[wire]

let part1 () =
    let instructions = input |> Array.map parseInstructions

    let wires =
        Array.map (fun x -> snd x, fst x) instructions
        |> Map.ofArray
        |> Collections.Generic.Dictionary

    let results = new Collections.Generic.Dictionary<string, uint16>()

    let result = calculate wires results "a"
    printfn "%A" result

let part2 () =
    let instructions = input |> Array.map parseInstructions

    let wires =
        Array.map (fun x -> snd x, fst x) instructions
        |> Map.ofArray
        |> Collections.Generic.Dictionary

    let results = new Collections.Generic.Dictionary<string, uint16>()

    let result = calculate wires results "a"
    wires["b"] <- { WireInstruction.LeftOperand = Convert.ToString result; RightOperand = ""; Instr = "SET" }

    let results = new Collections.Generic.Dictionary<string, uint16>()
    let result = calculate wires results "a"

    printfn "%A" result