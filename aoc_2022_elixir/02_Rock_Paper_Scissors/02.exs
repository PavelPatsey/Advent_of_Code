ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "get_shape_score" do
    assert Day02.get_shape_score("X") == 0
    assert Day02.get_shape_score("Y") == 1
    assert Day02.get_shape_score("Z") == 2
  end

  test "get_round_outcome" do
    assert Day02.get_round_outcome("A", "X") == 3
    assert Day02.get_round_outcome("A", "Y") == 6
    assert Day02.get_round_outcome("A", "Z") == 0
  end
end

defmodule Day02 do
  @shape_index %{
    "A" => 0,
    "B" => 1,
    "C" => 2,
    "X" => 0,
    "Y" => 1,
    "Z" => 2
  }

  @round_outcome_matrix {
    {3, 6, 0},
    {0, 3, 6},
    {6, 0, 3}
  }

  def read_input do
    {:ok, file} = File.read("./test_input")

    String.trim(file)
    |> String.split("\n")
    |> Enum.map(&String.split/1)
  end

  def get_total_round_score(elf_move, my_move) do
    get_round_outcome(elf_move, my_move) + get_shape_score(my_move)
  end

  def get_round_outcome(elf_move, my_move) do
    elem(elem(@round_outcome_matrix, @shape_index[elf_move]), @shape_index[my_move])
  end

  def get_shape_score(my_move) do
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
