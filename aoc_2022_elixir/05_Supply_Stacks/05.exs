defmodule Day05 do
  def read_input() do
    {:ok, file} = File.read("./test_input")

    [stacks_str, moves_str] =
      file
      |> String.replace("\r", "")
      |> String.split("\n\n")

    stacks =
      stacks_str
      |> String.split("\n")
      |> Enum.map(&String.split(&1, ""))
      |> Enum.zip()
      |> Enum.map(&Tuple.to_list/1)
      |> Enum.map(&Enum.reverse/1)
      |> Enum.filter(fn x -> hd(x) not in [" ", ""] end)
      |> Enum.map(fn x -> tl(x) end)
      |> Enum.map(fn x -> Enum.filter(x, fn x -> x != " " end) end)
      |> Enum.map(&Enum.reverse/1)

    moves =
      moves_str
      |> String.trim()
      |> String.split("\n")
      |> Enum.map(&String.split/1)
      |> Enum.map(fn x ->
        [_, x1, _, x2, _, x3] = x
        [x1, x2, x3]
      end)
      |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)
      |> Enum.map(fn x ->
        [x1, x2, x3] = x
        [x1, x2 - 1, x3 - 1]
      end)

    [stacks, moves]
  end
end

[stacks, moves] = Day05.read_input()
IO.inspect(stacks)
IO.inspect(moves)
