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
        except Exception as Error:
            return error


pdef insert_products(v):
    vs = str(v)
    q = "insert into products(name,buying_price,selling_price,stock_quantity) "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q


