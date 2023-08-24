ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "Shape score X" do
    assert Day02.get_your_shape_score("X") == 0
  end
end

defmodule Day02 do
  def read_input do
    {:ok, file} = File.read("./test_input")

    String.trim(file)
    |> String.split("\n")
    |> Enum.map(&String.split/1)
  end

  #   def get_total_round_score(elf_move, my_move) do
  #     1
  #   end

  #   def get_round_outcome(elf_move, my_move) do
  #     case {elf_move, my_move} do
  #       {"A", "X"} -> 0
  #     end
  #   end

  def get_your_shape_score(my_move) do
    case my_move do
      "X" -> 0
      "Y" -> 1
      "Z" -> 2
      _ -> "Incorrect shape"
    end
  end
end

rounds = Day02.read_input()

Day02.get_round_outcome("A", "X") |> IO.inspect()
