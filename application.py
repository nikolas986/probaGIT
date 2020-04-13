from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more1(): #ovo je fja koju traži onaj kada se kuca u html {{ url_for('more1') }} znači kada se pozove ova fja ona vraća adresu more.html
    return render_template("more.html") #ovde vraca more.html nikola stevanović 
#ovo sam ja dodao
@app.route("/bio")
def bio():
    return render_template("bio.html") #ovde sam napravio još jednu stranicu bio.html i na njoj sam stavio linkove ka druge dve
