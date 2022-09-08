from app import groceries
from app import dba
import pprint
import json

def write_list():
    grocery_list = groceries()
    dba_list = dba()
    with open('offers.txt', 'w') as reader:
        reader.write((json.dumps(grocery_list, indent=4)) + "\n")
        reader.write((json.dumps(dba_list, indent=4)) + "\n") 
    reader.close()

write_list()

""" def write_list():
    grocery_list = groceries()
    dba_list = dba()
    with open('offers.txt', 'w') as reader:
        for item in grocery_list:
            reader.write((str(item)) + "\n")
        for item in dba_list:
            reader.write((str(item)) + "\n")
    reader.close()

write_list() """