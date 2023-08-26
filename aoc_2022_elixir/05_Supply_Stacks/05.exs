defmodule Day05 do
  def read_input() do
    {:ok, file} = File.read("./test_input")

    [stacks_str, moves_str] = String.split(file, "\r\n\r\n")

    stacks_str =
      stacks_str
      |> String.split("\r\n")
      |> Enum.map(&String.split(&1, ""))

    asd =
      Enum.zip(stacks_str)
      |> IO.inspect()

    #   |> Enum.map(&Tuple.to_list/1)
    #   |> IO.inspect()
  end
end

Day05.read_input()
# [stacks, moves] = Day05.read_input()
# IO.inspect(stacks)
# IO.inspect(moves)
