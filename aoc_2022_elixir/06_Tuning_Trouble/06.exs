ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end

  test "test get_index" do
    assert Day06.get_index("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert Day06.get_index("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert Day06.get_index("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10

    assert Day06.get_index("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert Day06.get_index("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
  end
end

defmodule Day06 do
  def read_input(path) do
    {:ok, file} = File.read(path)

    file
    |> String.trim()
  end

  def get_index(data, number) do
    zipped =
      for n <- 1..number do
        Enum.drop(String.to_charlist(data), n - 1)
      end
      |> Enum.zip()
      |> Enum.with_index()

    index =
      zipped
      |> Enum.map(fn x ->
        {tuple, index} = x

        {tuple
         |> Tuple.to_list()
         |> MapSet.new()
         |> MapSet.size(), index}
      end)
      |> Enum.find(fn x -> elem(x, 0) == number end)
      |> elem(1)

    index + number
  end
end

data = Day06.read_input("./input")

Day06.get_index(data, 4)
|> IO.inspect(label: "part 1")

Day06.get_index(data, 14)
|> IO.inspect(label: "part 2")
