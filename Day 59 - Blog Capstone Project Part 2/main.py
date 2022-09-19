from flask import Flask, render_template
import requests


app = Flask(__name__)

api_endpoint = 'https://api.npoint.io/46c2a9265ef9ee56967d'
response = requests.get(url= api_endpoint)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts= all_posts)

    

@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/post/<post_id>')
def get_post(post_id):
    for post in all_posts:
        if int(post['id']) == int(post_id):
            return render_template('post.html', data= post)




if __name__ == "__main__":
    app.run(debug=True)