import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import pprint


URL = "https://etilbudsavis.dk/soeg/%C3%A6g"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")
offer_elements = results.find_all("li", class_="UniversalCardList__Item-sc-4v1xeg-4 klLrVZ")

stores = ["Rema 1000", "Netto"]
product_list  = []
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(today)
print(type(today))

for offer_element in offer_elements:
    case = {'store': offer_element.find(class_="BusinessLabel__BusinessLabelDiv-sc-iksnba-0 ijMGWk").text.strip(), 'name': offer_element.find("header").text.strip(), 'price':offer_element.find(class_="UniversalCardList___StyledStack-sc-4v1xeg-7 dYBUkI").text.strip(), 'fromDate': offer_element.find(itemprop="validFrom").get("content"), 'toDate': offer_element.find(itemprop="priceValidUntil").get("content")}
    if case['store'] in stores:
        #if today <= datetime(case['fromDate']) & today >= datetime(case['toDate']):
        #if today.format(datetime) <= datetime(datetime.fromisoformat(case['fromDate'][:-15])):
        #date_time_obj = datetime. strptime(date_time_str, '%d/%m/%y %H:%M:%S')
            product_list.append(case)


pprint.pprint(product_list)

""" for offer_element in offer_elements:
    print(offer_element.find(class_="BusinessLabel__BusinessLabelDiv-sc-iksnba-0 ijMGWk").text.strip())
    print(offer_element.find("header").text.strip())
    print(offer_element.find(class_="UniversalCardList___StyledStack-sc-4v1xeg-7 dYBUkI").text.strip())
    print(offer_element.find(itemprop="priceValidUntil").get("content"))
    print(offer_element.find(itemprop="validFrom").get("content"))
    print(datetime.fromisoformat(offer_element.find(itemprop="validThrough").get("content")[:-15]))
    datetime.fromisoformat(case['fromDate'][:-15])
    print()  """