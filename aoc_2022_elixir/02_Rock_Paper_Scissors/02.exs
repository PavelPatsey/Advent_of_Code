ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "the truth" do
    assert true
  end
end

{:ok, file} = File.read("./test_input")

IO.puts(file)
