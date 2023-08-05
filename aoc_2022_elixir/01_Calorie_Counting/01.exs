{:ok, file} = File.read("./input")

calories =
  file
  |> String.trim()
  |> String.split("\n\n")
  |> Enum.map(&String.split/1)
  |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)

calories_sums = Enum.map(calories, &Enum.sum/1)

Enum.max(calories_sums)
|> IO.inspect()

Enum.sort(calories_sums)
|> Enum.take(-3)
|> Enum.sum()
|> IO.inspect()
