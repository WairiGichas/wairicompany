import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=myduka user=postgres password=123nish")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM products")

# Retrieve query results
records = cur.fetchall()

#print(records)


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
        except Exception as Error:
            return error

sales = fetch_data("sales")
#print(sales) 

products = fetch_data("products")
#print(sales) 



def insert_products(v): 
            vs = str(v)
            q = "INSERT INTO products (pname,buying_price,selling_price,stock_quantity) VALUES" + vs
            cur.execute(q)
            conn.commit()
            return ("Product successfully added")
    
p1= insert_products(('batteries', 60,100,150))
print(p1)
data = fetch_data ("products")
print(data)

