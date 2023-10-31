import csv
from bs4 import BeautifulSoup

with open("vacancies.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    names_rows = next(csv_reader)

    for row in csv_reader:
        counter = 0
        dictionary = {}
        if '' in row:
            continue
        for i in row:
            dictionary[names_rows[counter]] = BeautifulSoup(i, "html.parser").get_text()
            counter += 1

        for key, value in dictionary.items():
            print(f"{key}: {value}")
        print()
