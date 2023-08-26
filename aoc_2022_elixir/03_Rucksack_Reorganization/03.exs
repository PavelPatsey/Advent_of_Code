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

  test "get_priority" do
    assert Day03.get_priority("p") == 16
    assert Day03.get_priority("L") == 38
    assert Day03.get_priority("P") == 42
    assert Day03.get_priority("v") == 22
    assert Day03.get_priority("Z") == 52
  end
end

defmodule Day03 do
  def read_input() do
    {:ok, file} = File.read("./input")
    String.trim(file) |> String.split()
  end

  def get_repeating_item(rucksack) do
    [part_1, part_2] =
      String.codepoints(rucksack)
      |> Enum.chunk_every(div(String.length(rucksack), 2))

    MapSet.intersection(MapSet.new(part_1), MapSet.new(part_2))
    |> Enum.at(0)
  end

  def get_priority(item) do
    item_code = hd(String.to_charlist(item))

    cond do
      item_code >= ?a and item_code <= ?z -> item_code - ?a + 1
      item_code >= ?A and item_code <= ?Z -> item_code - ?A + 27
    end
  end
end

rucksacks = Day03.read_input()

rucksacks
|> Enum.map(&Day03.get_repeating_item/1)
|> Enum.map(&Day03.get_priority/1)
|> Enum.sum()
|> IO.inspect()
