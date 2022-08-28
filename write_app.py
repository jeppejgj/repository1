from app import groceries

with open('offers.txt', 'w') as reader:
    reader.write(str(groceries()))
reader.close()