item_price=45
offer_perc=5
#sellin price ?
#discount_price=(actual_price*perce)/100

dic_price=(item_price*offer_perc)/100
price=item_price-dic_price
print(f"real price={price}")