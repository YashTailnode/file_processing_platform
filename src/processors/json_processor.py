import json

# json = [{"id": 1}, {"id": 2}]
with open("../../data.json", "r", encoding="utf-8") as file:
    counter = 0
    for row in file:
        parsed_row = json.loads(row)
        length = len(parsed_row)
        counter += length
    print(counter)
