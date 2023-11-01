import csv

with open("vacancies.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    names_rows = next(csv_reader)
    print(names_rows)

    length = len(names_rows)
    collection = []
    for row in csv_reader:
        if len(row) != length or "" in row:
            continue
        collection.append(row)
    print(collection)
