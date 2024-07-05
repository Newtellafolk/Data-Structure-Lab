"""ITEM1"""
import json as j
class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

def main():
    item_in = j.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
