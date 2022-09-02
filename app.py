from itertools import product
from unittest import skip
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import pprint

def groceries():
    URL_EGGS = "https://etilbudsavis.dk/soeg/%C3%A6g"
    page_eggs = requests.get(URL_EGGS)
    soup = BeautifulSoup(page_eggs.content, "html.parser")
    results_eggs = soup.find(id="main")
    resultset_eggs = results_eggs.find_all(
        "li", class_="UniversalCardList__Item-sc-4v1xeg-4 klLrVZ")
    
    URL_CHEESE = "https://etilbudsavis.dk/soeg/ost"
    page_cheese = requests.get(URL_CHEESE)
    soup = BeautifulSoup(page_cheese.content, "html.parser")
    results_cheese = soup.find(id="main")
    resultset_cheese = results_cheese.find_all(
        "li", class_="UniversalCardList__Item-sc-4v1xeg-4 klLrVZ")

    resultset_final = resultset_eggs + resultset_cheese

    product_list = []
    today = datetime.today()
    stores = ["Rema 1000", "Netto", "Føtex", "Coop365"]
    for resultset_element in resultset_final:
        case = {'store': resultset_element.find(class_="BusinessLabel__BusinessLabelDiv-sc-iksnba-0 ijMGWk").text.strip(), 'name': resultset_element.find("header").text.strip(), 'price': resultset_element.find(
            class_="UniversalCardList___StyledStack-sc-4v1xeg-7 dYBUkI").text.strip(), 'fromDate': resultset_element.find(itemprop="validFrom").get("content")[0:10], 'toDate': resultset_element.find(itemprop="priceValidUntil").get("content")[0:10]}
        from_date = datetime. strptime(case['fromDate'], '%Y-%m-%d')
        to_date = datetime. strptime(case['toDate'], '%Y-%m-%d')
        if case['store'] in stores:
            if from_date <= today <= to_date:
                product_list.append(case)
    return product_list

def dba():
    URL = "https://www.lauritz.com/en/auctions/?FText=syver"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="List_ItemListResult")
    resultset = results.find_all(
        class_="lotListControlX ADListNoHighLight") 

    negative_list = ["læder", "leather"]
    positive_list = ["stol"]

    product_list = []
    for resultset_element in resultset:  
        case = {'title': resultset_element.find(class_="pListLinkHeader").text.strip(), 'valuation': resultset_element.find(
            class_="valuation").text.strip(), 'current_bid': resultset_element.find(
            class_="status").text.strip()}
        title = case['title']
        if not any(word in title for word in negative_list):
            if any(word in title for word in positive_list):
                product_list.append(case)
    return product_list