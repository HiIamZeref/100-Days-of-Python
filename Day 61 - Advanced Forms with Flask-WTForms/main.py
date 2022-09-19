from cgitb import html
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "Haru"
Bootstrap(app= app)





class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label= "Log in")



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods= ['GET', 'POST'])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        if login.email.data == "admin@email.com" and login.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template('login.html', login=login)
        
    
    
    
        
    

if __name__ == '__main__':
    app.run(debug=True)