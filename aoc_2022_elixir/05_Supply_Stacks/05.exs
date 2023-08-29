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
      |> IO.inspect()

    stacks
  end
end

Day05.read_input()
# [stacks, moves] = Day05.read_input()
# IO.inspect(stacks)
# IO.inspect(moves)
