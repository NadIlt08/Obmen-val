import requests
import json
import pprint # красивый вывод текста в консоль


result = requests.get("https://open.er-api.com/v6/latest/USD")
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4) # отступы

p.pprint(data)