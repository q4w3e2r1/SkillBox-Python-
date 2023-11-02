import json
import re


def description_format(inform: str):
    parts = inform.split(". ")
    for i in range(len(parts)):
        parts[i] = parts[i].lower()
        parts[i] = parts[i].capitalize()

    return '.'.join(parts).replace('.', '. ')


def description_salary(inform: str):
    return "{:.3f}".format(float(inform))


def description_key_phrase(inform: str):
    temp = inform.upper() + '!'
    return temp[::]


def description_addition(inform: str):
    temp = inform.lower()
    return '...' + temp[::] + '...'


def description_reverse(inform: str):
    return inform[::-1]


def description_company_info(inform: str):
    result = re.sub(r'\([^()]*\)', '', inform)
    result = re.sub(r'\([^)]*\)', '', result)
    return result


def description_key_skills(inform: str):
    result = inform.replace('&nbsp', ' ')
    return result


text = input()
headings = input()

temp = text.split(';')
result = {}
for i in temp:
    information = i.split(':')
    key = information[0].replace(' ', '')
    if key in headings:
        for j in range(1, len(information)):
            result[key] = result.get(key, '') + information[j]

for key, value in result.items():
    value = value[1::]
    if key == 'description':
        result[key] = description_format(value)
    elif key == 'salary':
        result[key] = description_salary(value)
    elif key == 'key_phrase':
        result[key] = description_key_phrase(value)
    elif key == 'addition':
        result[key] = description_addition(value)
    elif key == 'reverse':
        result[key] = description_reverse(value)
    elif key == 'company_info':
        result[key] = description_company_info(value)
    elif key == 'key_skills':
        result[key] = description_key_skills(value)

json_output = json.dumps(result)
print(json_output)
