#STORE ALL PRODUCT NAMES IN A LIST AND ONLY PRINT THAT LIST. DO NOT FILTER THE QUESRY.
#DO NOT FILTER IN THE QUERY.
#1. RECORDS IS A LIST OF TUPLES
#2. Create an empty list to hold names
#3. For Loop - because it is list
#4. We append i while indexing . i.e. i[]
#5. Outside the loop we print.

import psycopg2

try:
    conn = psycopg2.connect("dbname=myduka user=postgres password=123nish")
    cur= conn.cursor()
except Exception as error:
    print(error)

def fetch_data(tbln):
        try:
            q = "SELECT * FROM " + tbln +  ";"
            cur.execute(q)
            records = cur.fetchall()
            return records
        except Exception as error:
            return error

        sales = fetch_data("sales")
        print(sales)    
        
        #def insert_data(tbln):
           # q = "INSERT INTO products (pname, buying_price, selling_price, stock_quantity) VALUES (Dasani-water,20,40,100)"
            
            
            #or  
        
             
def insert_product(v): 
            vs = str(v)
            q = "insert into products (pname,buying_price,selling_price,stock_quantity) values"+vs
            cur.execute(q)
            conn.commit()
            return ("Product added successfully")
    
p1= insert_product(('kiwi',60,100,150))
print(p1)
        
data = fetch_data("products")
print(data)