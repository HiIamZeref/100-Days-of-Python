from flask import Flask, render_template
import requests


app = Flask(__name__)


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<blog_id>")
def get_post(blog_id):
    for blog_post in all_posts:
        if int(blog_id) == int(blog_post['id']):
            request_post = blog_post

    print(request_post)

    return render_template('post.html', data=request_post)

if __name__ == "__main__":
    app.run(debug=True)
