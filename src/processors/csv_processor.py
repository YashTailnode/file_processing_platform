with open("../../data.csv", "r", encoding="utf-8") as file:
    counter = 0
    for row in file:
        counter += 1
    print(counter)
