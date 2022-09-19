from flask import Flask, render_template, request
import requests
import smtplib


app = Flask(__name__)

EMAIL = "########"
PASSWORD = "#########"

api_endpoint = 'https://api.npoint.io/46c2a9265ef9ee56967d'
response = requests.get(url= api_endpoint)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts= all_posts)

    

@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/contact/', methods= ['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user= EMAIL, password= PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs= EMAIL,
                msg= f"Nome: {request.form['name']} \n EMAIL: {request.form['email']} \n Phone: {request.form['phone']} \n Message: {request.form['message']} \n"
                

            )
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        return f"<h1> Successfully sent your message. </h1>"



@app.route('/post/<post_id>')
def get_post(post_id):
    for post in all_posts:
        if int(post['id']) == int(post_id):
            return render_template('post.html', data= post)



    
    





if __name__ == "__main__":
    app.run(debug=True)