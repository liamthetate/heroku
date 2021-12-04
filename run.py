import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = [] #list
    with open("data/company.json", "r") as json_data: #r = read  / data is from json file in data folder / json_data is an arribuary name
        data = json.load(json_data) #assigned the json file to the variable 'data'
    return render_template("about.html", page_title="About", company=data) #that 'data' then goes into a new variable 'company'

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member) #first member = the html file, the second is the one defined above, inside 'about_member(member_name)'


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # print(request.form.get("name") or print(request.form["email"])
        flash("Thanks {} we have recieved your message".format(
            request.form.get("name")))
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template('careers.html')

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True #delete this on submission
    )