from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


for p,v in bakery_stock.items():
    if food in bakery_stock.keys():
        print(f"{v} left")
    else:
        print('we dont have this iteam')


if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

    quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")
