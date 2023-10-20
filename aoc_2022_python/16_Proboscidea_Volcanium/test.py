travels = ["a", "b", "c", "d"]
released_pressures = [1, 6, 3, 5]

zipped = zip(travels, released_pressures)


max_zipped = max(zipped, key=lambda x: x[1])
print(max_zipped)
