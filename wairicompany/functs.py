import psycopg2


try:
    conn = psycopg2.connect("dbname=wairicompany user=postgres password=123nish")
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


products = fetch_data("customers")

