# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dialogue.db'
app.config['SECRET_KEY'] = 'e0026030e136b7ef108b8e2e'
db: SQLAlchemy = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.String(length=60), nullable=False)





class RegistrationForms(FlaskForm):
    username = StringField(label='username')
    password = PasswordField(label='password')
    password2 = PasswordField(label='repeat password')
    submit = SubmitField(label='submit')


@app.route('/home')
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
    return render_template('home.html')


@app.route('/infos')
def info():
    return render_template('infos.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/typeandhear')
def type_and_hear():
    return render_template('type_and_hear.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    form = RegistrationForms()
    if form.validate_on_submit():
        user_to_create = Item(name=form.username.data,
                              price=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
