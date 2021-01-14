import requests

print(requests.__version__)
r = requests.get('https://raw.githubusercontent.com/lida9/404-lab1/main/script.py')
print(r.text)
