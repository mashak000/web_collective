import os

from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
from werkzeug.utils import secure_filename
import random




app = Flask(__name__)
 
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'pdf', 'psd', 'tiff']

os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)

db = SQL("sqlite:///applications.db")

dbcity = SQL("sqlite:///cities.db")

#check if file is with correct extension
def allowed_file(filename):
    partsname = filename.rsplit('.')
    if partsname[-1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/opencall")
def opencall():
    return render_template("opencall.html")

@app.route("/blog")
def blog():
    #open file with the list of links to posts
    #get a random post from it and pass it to the page
    posts = ["858","846", "847", "848", "855", "845", "820", "840", "811", "793", "781", "764", "741"]
    postik = random.choice(posts)
    return render_template("blog.html", postik = postik)

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/form", methods=["GET", "POST"])
def form():

    #user reached via POST
    if request.method == "POST":
        
        
        rows = db.execute("SELECT email FROM application")
        
        #тут нужны всяческие проверки вводимых данных !!!!!!
        for row in rows: 
            if request.form.get("email") == row["email"]:
                return render_template("stop.html")
        
        
            
        #загрузка файла в отдельную папку 
        file = request.files["fileapp"]
        print(file.filename)

    
        
        #нужна проверка что файл входит в обозначенные расширения 
        if file and allowed_file(file.filename) == True:
            if request.form.get("radio2") == "yes":
                filename = (request.form.get("email") + "." + secure_filename(file.filename))
                file.save(os.path.join(app.instance_path, 'htmlfi', filename))
                db.execute("INSERT INTO application (email, name) VALUES (?, ?)", request.form.get("email"), request.form.get("name"))
                return render_template("success.html")
                # на введенный в форме имейл должен прийти письмо подтверждение что пришла заявка
            else:
                return render_template("thief.html")
        else:
            return render_template("incorrectfile.html")



    # User reached route via GET (as by clicking a link or via redirect)
    else:
        #upload cities into datalist
        cities = dbcity.execute("SELECT name FROM cities")
    
        return render_template("form.html", cities = cities)