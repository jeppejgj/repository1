import requests

URL = "https://etilbudsavis.dk/"
page = requests.get(URL)

print(page.text)