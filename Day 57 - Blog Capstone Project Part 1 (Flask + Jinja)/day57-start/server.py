from urllib import response
from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

today = datetime.now()
year = today.year




@app.route("/")
def home():
    global year
    name = "Felipe Coimbra"
    return render_template('index.html', year=year, name=name)


@app.route("/guess/<name>")
def guess_name(name: str):
    proper_name = name.capitalize()
    age_url = "https://api.agify.io"
    gender_url = "https://api.genderize.io"
    params = {
        "name": name
    }

    age_response = requests.get(url= age_url, params= params)
    age_response.raise_for_status()
    age_data = age_response.json()

    gender_response = requests.get(url= gender_url, params= params)
    gender_response.raise_for_status()
    gender_data = gender_response.json()

    return render_template('guess.html',age_data= age_data, gender_data= gender_data, name=proper_name)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts= all_posts)




if __name__ == "__main__":
    app.run(debug=True)