ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end
end

defmodule Day04 do
  def read_input() do
    {:ok, file} = File.read("./test_input")

    file
    |> String.split()
    |> Enum.map(&String.split(&1, ["-", ","]))
    |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)
  end
end

assignments = Day04.read_input() |> IO.inspect()
