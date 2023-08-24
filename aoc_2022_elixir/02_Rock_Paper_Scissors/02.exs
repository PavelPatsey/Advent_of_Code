ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end
end

defmodule Day02 do
  def read_input do
    {:ok, file} = File.read("./test_input")

    String.trim(file)
    |> String.split("\n")
    |> Enum.map(&String.split/1)
  end
end

rounds = Day02.read_input()
