ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "test get_stacks_after_move" do
    assert Day05.get_stacks_after_move(
             [["N", "Z", 1], ["D", "C", "M", 2], ["P", 3]],
             [0, 2, 1],
             1
           ) ==
             [["N", "Z", 1], ["D", "C", "M", 2], ["P", 3]]

    assert Day05.get_stacks_after_move(
             [["N", "Z", 1], ["D", "C", "M", 2], ["P", 3]],
             [1, 2, 1],
             1
           ) ==
             [["D", "N", "Z", 1], ["C", "M", 2], ["P", 3]]

    assert Day05.get_stacks_after_move(
             [["D", "N", "Z", 1], ["C", "M", 2], ["P", 3]],
             [3, 1, 3],
             1
           ) ==
             [[1], ["C", "M", 2], ["Z", "N", "D", "P", 3]]

    assert Day05.get_stacks_after_move(
             [["D", "N", "Z", 1], ["C", "M", 2], ["P", 3]],
             [3, 1, 3],
             1
           ) ==
             [[1], ["C", "M", 2], ["Z", "N", "D", "P", 3]]
  end
end

defmodule Day05 do
  def read_input(path) do
    {:ok, file} = File.read(path)

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
      |> Enum.map(fn x ->
        [head | tail] = x
        [String.to_integer(head) | tail]
      end)
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

    [stacks, moves]
  end

  def get_stacks_after_moving(stacks, [], _), do: stacks

  def get_stacks_after_moving(stacks, moves, part) do
    stacks = get_stacks_after_move(stacks, hd(moves), part)
    get_stacks_after_moving(stacks, tl(moves), part)
  end

  def get_stacks_after_move(stacks, [items_number, from_stack, to_stack], part) do
    items =
      Enum.filter(stacks, fn x ->
        List.last(x) == from_stack
      end)
      |> hd()
      |> Enum.take(items_number)

    stacks =
      stacks
      |> Enum.map(fn x ->
        if List.last(x) == from_stack do
          Enum.drop(x, items_number)
        else
          x
        end
      end)

    items =
      if part == 1 do
        Enum.reverse(items)
      else
        items
      end

    stacks
    |> Enum.map(fn x ->
      if List.last(x) == to_stack do
        Enum.concat(items, x)
      else
        x
      end
    end)
  end
end

[stacks, moves] = Day05.read_input("./input")
# IO.inspect(stacks)
# IO.inspect(moves)

Day05.get_stacks_after_moving(stacks, moves, 1)
|> Enum.map(&hd/1)
|> Enum.join()
|> IO.inspect()
