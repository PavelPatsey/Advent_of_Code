defmodule Day03 do
  def read_input() do
    {:ok, file} = File.read("./test_input")
    String.trim(file) |> String.split()
  end
end

items = Day03.read_input()
