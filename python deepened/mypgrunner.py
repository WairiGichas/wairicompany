from mytestpostgress import insert_products,fetch_data

# Request user for 4 inputs, insert to the table and only return that on record with its ID


pname = input('product name: ')
buying_price = float(input('buying_price: '))
selling_price=float(input('selling_price: '))
stock_quantity=int(input('stock_quantity: '))
#() is a tuple [] is a list

data =("pname,buying_price,selling_price,stock_quantity")
insert_products(data) #data here stands in for a tuple
res = fetch_data('products') #returns list of tuples i.e. [(),(),(),()] 
print(res[-1]) # -1 will give the last tuple



