import requests
from bs4 import BeautifulSoup

URL = "https://etilbudsavis.dk/soeg/%C3%A6g"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")
offer_elements = results.find_all("li", class_="UniversalCardList__Item-sc-4v1xeg-4 klLrVZ")



for offer_element in offer_elements:
    print(offer_element.find(class_="BusinessLabel__BusinessLabelDiv-sc-iksnba-0 ijMGWk").text.strip())
    print(offer_element.find("header").text.strip())
    print(offer_element.find(class_="UniversalCardList___StyledStack-sc-4v1xeg-7 dYBUkI").text.strip())
    print(offer_element.find(itemprop="priceValidUntil").get("content"))
    print(offer_element.find(itemprop="validFrom").get("content"))
    print(offer_element.find(itemprop="validThrough").get("content"))
    #print(offer_element.find(content, itemprop="validThrough"))
    #print(offer_element.find('meta', attrs={'itemprop':'validFrom'}).text)
    print()