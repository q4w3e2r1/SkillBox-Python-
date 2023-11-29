import requests
import json

url = 'https://swapi.dev/api/starships/10/'
response = requests.get(url)
text_file = 0

if response.status_code == 200:
    info = json.loads(response.text)
    result = {}
    attr = ["max_atmosphering_speed", "starship_class", "pilots"]
    result["ship_name"] = info["name"]
    for key in attr:
        result[key] = info[key]

    attr_pilot = ["name", "height", "mass", "homeworld"]
    temp = []

    for pilot in result["pilots"]:
        response_pilot = requests.get(pilot)

        if response_pilot.status_code == 200:
            content_pilot = json.loads(response_pilot.text)
            result_pilot = {}
            for key in attr_pilot:
                result_pilot[key] = content_pilot[key]

            current_home = 0
            response_home = requests.get(result_pilot["homeworld"])
            if response_home.status_code == 200:
                content_home = json.loads(response_home.text)
                current_home = content_home["name"]

            result_pilot["homeworld_url"] = result_pilot["homeworld"]
            result_pilot["homeworld"] = current_home
            temp.append(result_pilot)

    result["pilots"] = temp
    text_file = result
    result = json.dumps(result, indent=4)
    print(result)

    with open('starship_info.json', 'w') as f:
        json.dump(text_file, f, indent=4)
else:
    print('Ошибка при отправке запроса:', response.status_code)
