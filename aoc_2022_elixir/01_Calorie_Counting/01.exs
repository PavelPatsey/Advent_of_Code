{:ok, file} = File.read("./input")

calories =
  file
  |> String.trim()
  |> String.split("\n\n")
  |> Enum.map(&String.split/1)
  |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)

calories_sums = Enum.map(calories, &Enum.sum/1)

IO.puts(Enum.max(calories_sums))
