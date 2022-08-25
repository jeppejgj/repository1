import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import pprint

URL = "https://etilbudsavis.dk/soeg/%C3%A6g"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")
offer_elements = results.find_all(
    "li", class_="UniversalCardList__Item-sc-4v1xeg-4 klLrVZ")

stores = ["Rema 1000", "Netto", "Føtex"]
product_list = []
today = datetime.today()

for offer_element in offer_elements:
    case = {'store': offer_element.find(class_="BusinessLabel__BusinessLabelDiv-sc-iksnba-0 ijMGWk").text.strip(), 'name': offer_element.find("header").text.strip(), 'price': offer_element.find(
        class_="UniversalCardList___StyledStack-sc-4v1xeg-7 dYBUkI").text.strip(), 'fromDate': offer_element.find(itemprop="validFrom").get("content")[0:10], 'toDate': offer_element.find(itemprop="priceValidUntil").get("content")[0:10]}
    from_date = datetime. strptime(case['fromDate'], '%Y-%m-%d')
    to_date = datetime. strptime(case['toDate'], '%Y-%m-%d')
    if case['store'] in stores:
        if today >= from_date and today <= to_date:
            product_list.append(case)

pprint.pprint(product_list)
