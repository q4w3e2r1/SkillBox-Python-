import csv
from bs4 import BeautifulSoup


def get_statistics_salaries(collections):
    sorted_list = sorted(collections, key=lambda x: x['salary'], reverse=True)

    names_employer = [item['employer_name'] for item in sorted_list]
    names_area = [item['area_name'] for item in sorted_list]
    names = [item['name'] for item in sorted_list]
    salary = [item['salary'] for item in sorted_list]

    result = 'Самые высокие зарплаты: \n'
    for i in range(min(len(salary), 10)):
        result += f'  {i + 1}) {names[i]} в компании \"{names_employer[i]}\" - {int(salary[i])} рублей (г. {names_area[i]}) \n'

    print(result)

    result = 'Самые низкие зарплаты: \n'
    for i in range(min(len(salary), 10)):
        result += f'  {i + 1}) {names[len(names) - 1 - i]} в компании \"{names_employer[len(names) - 1 - i]}\" - {int(salary[len(names) - 1 - i])} рублей (г. {names_area[len(names) - 1 - i]}) \n'

    print(result)


def get_statistics_city(collections):
    result_dict = {}

    for dictionary in collections:
        key1 = list(dictionary.keys())[6]
        key2 = list(dictionary.keys())[7]
        city = dictionary[key1]
        salary = dictionary[key2]
        if city in result_dict:
            result_dict[city] = max(result_dict[city], salary)
        else:
            result_dict[city] = salary


    result = f'Из {len(result_dict)} городов, самые высокие средние ЗП:\n'
    i = 0
    for key, value in result_dict.items():
        result += f'  {i + 1}) {key} - средняя зарплата {int(value)} рублей (1 вакансия)\n'
        i += 1
    print(result)






with open("vacancies.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    names_rows = next(csv_reader)
    collections = []
    for row in csv_reader:
        counter = 0
        dictionary = {}
        if '' in row:
            continue
        for i in row:
            dictionary[names_rows[counter]] = BeautifulSoup(i, "html.parser").get_text()
            counter += 1

        try:
            salary_from = int(dictionary['salary_from'])
            salary_to = int(dictionary['salary_to'])
            dictionary['salary'] = (salary_from + salary_to) / 2
        except ValueError:
            continue
        collections.append(dictionary)

    #get_statistics_salaries(collections)
    get_statistics_city(collections)
