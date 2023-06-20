from flask import Flask, render_template
from functs import fetch_data
app = Flask(__name__) 


@app.route('/') #landing page of our web application
def home():
        
        name="Wairimu" 

       
        return render_template("index.html", name = name)

@app.route("/customers")  # @ binds function about path
def customers():
    customers = fetch_data ("customers")
  
    print(customers)
    return render_template("customers.html", customers = customers)



app.run()