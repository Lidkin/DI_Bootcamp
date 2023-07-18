
def shopping(items_purchase, wallet):
    
    store_list = []
    for key, value in items_purchase.items():
        store_list.append(f"{key}: {value}")


    my_store_list = ', '.join(store_list)

    print(f"list of the items: {my_store_list}.\nMoney in the wallet: {wallet}")

    my_wallet = int(wallet.replace("$", "").replace(",", ""))
    shopping_cart = []
    sum = 0
    for key, value in items_purchase.items():
        item_price = int(value.replace("$", "").replace(",", ""))
        sum += item_price
        if sum <= my_wallet:
            shopping_cart.append(key)
        else:
            sum -= item_price   
    if len(shopping_cart) == 0:
        print("I can buy: Nothing")
    else:     
        print("I can buy:", ', '.join(sorted(shopping_cart)))
      

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
wallet = "$300"  
shopping(items_purchase, wallet)

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}
wallet = "$100" 
shopping(items_purchase, wallet)

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}
wallet = "$1" 
shopping(items_purchase, wallet)








