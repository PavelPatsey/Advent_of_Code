ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "get_repeating_item" do
    assert Day03.get_repeating_item("qwertqs1df") == "q"
    assert Day03.get_repeating_item("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert Day03.get_repeating_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert Day03.get_repeating_item("PmmdzqPrVvPwwTWBwg") == "P"
  end
end

defmodule Day03 do
  def read_input() do
    {:ok, file} = File.read("./test_input")
    String.trim(file) |> String.split()
  end

  def get_repeating_item(rucksack) do
    [part_1, part_2] =
      String.codepoints(rucksack)
      |> Enum.chunk_every(div(String.length(rucksack), 2))

    MapSet.intersection(MapSet.new(part_1), MapSet.new(part_2))
    |> Enum.at(0)
  end
end

rucksacks =
  Day03.read_input()
  |> IO.inspect()
