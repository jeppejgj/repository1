import requests
from bs4 import BeautifulSoup

URL = "https://etilbudsavis.dk/soeg/%C3%A6g"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")
offer_elements = results.find_all("li", class_="UniversalCardList__Item-sc-4v1xeg-4 klLrVZ")



for offer_element in offer_elements:
    #header_element = offer_element.find("header")
    #price_element = offer_element.find(class_="Stack__Item-sc-u1ffod-2 Stack___StyledItem-sc-u1ffod-3 cWwVbp kgTTno")
    #location_element = offer_element.find("p", class_="location")
    print(offer_element.find(class_="BusinessLabel__BusinessLabelDiv-sc-iksnba-0 ijMGWk").text.strip())
    print(offer_element.find("header").text.strip())
    print(offer_element.find(class_="UniversalCardList___StyledStack-sc-4v1xeg-7 dYBUkI").text.strip())
    print(offer_element.find("meta", itemprop="priceValidUntil"))
    print(offer_element.find(itemprop="validFrom")[0])
    print(str(offer_element.find("meta", itemprop="validThrough").unwrap()))
    #print(location_element.text.strip())
    print()