ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "test is_contains" do
    assert Day04.is_contains([2, 4, 6, 8]) == false
    assert Day04.is_contains([6, 6, 4, 6]) == true
    assert Day04.is_contains([3, 7, 2, 8]) == true
    assert Day04.is_contains([2, 8, 3, 7]) == true
  end
end

defmodule Day04 do
  def read_input() do
    {:ok, file} = File.read("./input")

    file
    |> String.split()
    |> Enum.map(&String.split(&1, ["-", ","]))
    |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)
  end

  def is_contains([a1, a2, b1, b2]) do
    (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2)
  end
end

assignments = Day04.read_input()

Enum.filter(assignments, &Day04.is_contains/1)
|> length()
|> IO.inspect()
