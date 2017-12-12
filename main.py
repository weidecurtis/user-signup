from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect('/signup')

@app.route("/home", methods=['POST'])
def home():
    return render_template('home.html')

@app.route('/signup')
def display_signup_form():
    return render_template('home.html')

@app.route("/signup", methods=['POST'])
def signup():

    username = request.form['Username']
    password = request.form['Password']
    verify_password = request.form['Verify_Password']
    email = request.form['Email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) < 1:
        username = ''
        username_error = 'Please enter a valid username.'
    elif ' ' in username:
        username_error = "Please don't use spaces."
    else:
        username = username
        if len(username) < 3 or len(username) > 20:
            username_error = 'Please have a username between 3 and 20 characters!'

    if len(password) < 1:
        password = ''
        password_error = 'Please enter a valid password.'
    elif ' ' in password:
        password_error = "Please don't use spaces"
    else:
        password = password
        if len(password) < 3 or len(password) > 20:
            password = ''
            password_error = 'Please have a password between 3 and 20 characters!'

    if len(verify_password) < 1:
        verify_password_error = 'Please verify your password.'
    else:
        if password == verify_password:
            verify_password = verify_password
        else:
            verify_password_error = 'Please make sure your passwords match!'

    if email:
        if '@' not in email:
            email_error = "Please provide a valid email."
        elif '.' not in email:
            email_error = "Please provide a valid email." 
        else:
            email = email
            if len(email) < 3 or len(email) > 20:
                email_error = 'Please have an email between 3 and 20 characters!' 


    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('home.html',
        username = username,
        email = email,
        email_error = email_error,
        username_error = username_error,
        password_error = password_error,
        verify_password_error = verify_password_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(username)
app.run()