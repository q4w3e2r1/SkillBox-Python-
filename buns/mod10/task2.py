import requests
import re

url = "http://www.columbia.edu/~fdc/sample.html"
#url = input("Введите адрес сайта")
def get_h3_tag(url):
    response = requests.get(url)
    text = response.text

    pattern = re.compile(r'<h3.*?>(.*?)</h3>')
    result = pattern.findall(text)

    return result


subheadings_list = get_h3_tag(url)
print(subheadings_list)
