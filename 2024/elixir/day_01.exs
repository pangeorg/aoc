defmodule Part1 do
  def run do
    {l1, l2} =
      File.stream!("../input/day_01.txt")
      |> Stream.map(&String.trim/1)
      |> Stream.reject(&(&1 == ""))
      |> Stream.map(fn line ->
        case String.split(line) do
          [a, b] ->
            {num_a, _} = Integer.parse(a)
            {num_b, _} = Integer.parse(b)
            {num_a, num_b}

          _ ->
            nil
        end
      end)
      |> Stream.reject(&is_nil/1)
      |> Enum.reduce({[], []}, fn {a, b}, {acc1, acc2} ->
        {[a | acc1], [b | acc2]}
      end)

    {l1, l2} = {Enum.sort(l1), Enum.sort(l2)}

    result =
      Enum.zip(l1, l2)
      |> Enum.reduce(0, fn {a, b}, acc ->
        acc + abs(a - b)
      end)

    IO.puts(result)
  end
end

defmodule Part2 do
  def run do
    {l1, l2} =
      File.stream!("../input/day_01.txt")
      |> Stream.map(&String.trim/1)
      |> Stream.reject(&(&1 == ""))
      |> Stream.map(fn line ->
        case String.split(line) do
          [a, b] ->
            {num_a, _} = Integer.parse(a)
            {num_b, _} = Integer.parse(b)
            {num_a, num_b}

          _ ->
            nil
        end
      end)
      |> Stream.reject(&is_nil/1)
      |> Enum.reduce({[], []}, fn {a, b}, {acc1, acc2} ->
        {[a | acc1], [b | acc2]}
      end)

    counter = l2 |> Enum.frequencies()

    result =
      l1
      |> Enum.reduce(0, fn item, acc ->
        if Map.has_key?(counter, item) do
          v = Map.get(counter, item)
          acc + v * item
        else
          acc
        end
      end)

    IO.puts(result)
  end
end

Part2.run()
