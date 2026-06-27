with open("../../data.xml", "r", encoding="utf-8") as file:
    counter = 0
    for row in file:
        printed_row = row.strip()
        counter += 1
    print(counter)
