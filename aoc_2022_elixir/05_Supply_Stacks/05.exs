ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "test get_stacks_after_move" do
    assert Day05.get_stacks_after_move(
             %{1 => ["N", "Z"], 2 => ["D", "C", "M"], 3 => ["P"]},
             [0, 2, 1],
             1
           ) ==
             %{1 => ["N", "Z"], 2 => ["D", "C", "M"], 3 => ["P"]}

    assert Day05.get_stacks_after_move(
             %{1 => ["N", "Z"], 2 => ["D", "C", "M"], 3 => ["P"]},
             [1, 2, 1],
             1
           ) ==
             %{1 => ["D", "N", "Z"], 2 => ["C", "M"], 3 => ["P"]}

    assert Day05.get_stacks_after_move(
             %{1 => ["D", "N", "Z"], 2 => ["C", "M"], 3 => ["P"]},
             [3, 1, 3],
             1
           ) ==
             %{1 => [], 2 => ["C", "M"], 3 => ["Z", "N", "D", "P"]}

    assert Day05.get_stacks_after_move(
             %{1 => ["D", "N", "Z"], 2 => ["C", "M"], 3 => ["P"]},
             [3, 1, 3],
             2
           ) ==
             %{1 => [], 2 => ["C", "M"], 3 => ["D", "N", "Z", "P"]}
  end
end

defmodule Day05 do
  def read_input(path) do
    file = File.read!(path)

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
      |> Enum.map(fn x -> Enum.filter(x, fn x -> x != " " end) end)
      |> Map.new(fn x -> {String.to_integer(hd(x)), Enum.reverse(tl(x))} end)

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

    {stacks, moves}
  end

  def get_stacks_after_moving(stacks, [], _), do: stacks

  def get_stacks_after_moving(stacks, moves, part) do
    stacks = get_stacks_after_move(stacks, hd(moves), part)

    get_stacks_after_moving(stacks, tl(moves), part)
  end

  def get_stacks_after_move(stacks, [items_number, from_stack, to_stack], part) do
    items =
      stacks[from_stack]
      |> Enum.take(items_number)

    items =
      if part == 1 do
        Enum.reverse(items)
      else
        items
      end

    %{
      stacks
      | from_stack => Enum.drop(stacks[from_stack], items_number),
        to_stack => Enum.concat(items, stacks[to_stack])
    }
  end
end

{stacks, moves} = Day05.read_input("./input")

Day05.get_stacks_after_moving(stacks, moves, 1)
|> Map.values()
|> Enum.map(&hd/1)
|> Enum.join()
|> IO.inspect(label: "part 1")

Day05.get_stacks_after_moving(stacks, moves, 2)
|> Map.values()
|> Enum.map(&hd/1)
|> Enum.join()
|> IO.inspect(label: "part 2")
