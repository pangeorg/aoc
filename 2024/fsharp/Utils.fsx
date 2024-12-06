type Map<'a, 'b when 'a : comparison> with
    member this.Get(key: 'a, value: 'b) =
        match this.TryFind key with
        | Some v -> v
        | None -> value