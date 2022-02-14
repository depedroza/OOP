import RetailItemClass as r


def main():
    retailInfo = set_info()
    display_info(retailInfo)


def set_info():
    item_creation = []
    itemInv = {
        "Item#1": {"Description": "Jacket", "Inventory": "12", "Price": "59.95"},
        "Item#2": {
            "Description": "Designer Jeans",
            "Inventory": "40",
            "Price": "34.95",
        },
        "Item#3": {"Description": "Shirt", "Inventory": "20", "Price": "24.95"},
    }

    for i in range(1, 4):
        desc = itemInv[f"Item#{i}"]["Description"]
        inv = itemInv[f"Item#{i}"]["Inventory"]
        price = itemInv[f"Item#{i}"]["Price"]

        my_item = r.Item(desc, inv, price)
        item_creation.append(my_item)
    return item_creation


# included here for proof of three created items and access to the same
def display_info(retailInfo):
    print(retailInfo)
    print()
    for i in retailInfo:
        print(i.get_description())
        print(i.get_inventory())
        print(i.get_price())
        print()


main()
