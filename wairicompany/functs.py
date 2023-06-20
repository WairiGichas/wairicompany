import psycopg2


try:
    conn = psycopg2.connect("dbname=wairicompany user=postgres password=123nish")
    cur= conn.cursor()
except Exception as error:
    print(error)

def fetch_data(tbname):
        try:
            q = "SELECT * FROM " + tbname +  ";"
            cur.execute(q)
            records = cur.fetchall()
            return records
        except Exception as error:
            return error

def insert_customers(v):
    vs = str(v)
    q = "insert into products(firstname,lastname,email,phone) "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q



