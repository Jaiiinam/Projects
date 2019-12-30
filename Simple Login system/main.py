from flask import Flask, jsonify, request, json, Response, render_template, flash, redirect,url_for, session
from flask_bootstrap import Bootstrap
import loginRegister, tables
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_user, LoginManager, login_required, logout_user, UserMixin
from flask_bcrypt import Bcrypt
from datetime import timedelta 



app = Flask(__name__, template_folder='Templates')
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///credentials.db'
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



@login_manager.user_loader
def load_user(id):
    return tables.User.query.get(int(id))


@app.route('/whoAreWe')
def whoAreWe():
    return render_template('whoAreWe.html', title='Who are we?')

    
@app.route('/home')
@login_required
def home():
    return render_template('home.html', title='Home')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated == True:
        return redirect(url_for('home'))

    form = loginRegister.LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = tables.User.query.filter_by(username=form.username.data).first()
        
        login_user(user, remember=form.remember.data)
        return redirect(url_for('home'))


    return render_template('login.html', title='Login', form=form) 




@app.route('/register', methods=['POST', 'GET'])
def register():

    if current_user.is_authenticated == True:
        return redirect(url_for('home'))

        
    form = loginRegister.RegistrationForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = tables.User(username=form.username.data, password_hash=password)
            tables.db.session.add(user)
            tables.db.session.commit()
            flash('Thank you for registering!', 'success')
            return redirect(url_for('register'))

        else:
            flash('Sorry, you must meet all the given requirements', 'error')
  
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    tables.db.init_app(app)
    app.run(host = '127.0.0.1', port=8080, debug=1)