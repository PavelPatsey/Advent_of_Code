ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "get_total_round_score" do
    assert Day02.get_total_round_score(["A", "Y"]) == 8
    assert Day02.get_total_round_score(["B", "X"]) == 1
    assert Day02.get_total_round_score(["C", "Z"]) == 6
  end

  test "get_total_round_score_2" do
    assert Day02.get_total_round_score_2(["A", "Y"]) == 4
    assert Day02.get_total_round_score_2(["B", "X"]) == 1
    assert Day02.get_total_round_score_2(["C", "Z"]) == 7
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
    {:ok, file} = File.read("./input")

    String.trim(file)
    |> String.split("\n")
    |> Enum.map(&String.split/1)
  end

  def get_total_round_score([elf_move, my_move]) do
    round_outcome =
      elem(elem(@round_outcome_matrix, @shape_index[elf_move]), @shape_index[my_move])

    shape_score =
      case my_move do
        "X" -> 1
        "Y" -> 2
        "Z" -> 3
      end

    round_outcome + shape_score
  end

  def get_total_round_score_2([elf_move, my_move]) do
    round_outcome =
      case my_move do
        "X" -> 0
        "Y" -> 3
        "Z" -> 6
      end

    shape_score =
      elem(@round_outcome_matrix, @shape_index[elf_move])
      |> Tuple.to_list()
      |> Enum.find_index(fn x -> x == round_outcome end)
      |> Kernel.+(1)

    round_outcome + shape_score
  end
end

rounds = Day02.read_input()

Enum.map(rounds, &Day02.get_total_round_score/1)
|> Enum.sum()
|> IO.inspect()

Enum.map(rounds, &Day02.get_total_round_score_2/1)
|> Enum.sum()
|> IO.inspect()
