from flask import render_template, redirect, url_for
from app import app, db,login_manager
from .forms import LoginForm, RegisterForm
from flask_login import login_required, login_user, current_user, logout_user
from .models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/dashboard', methods =[ 'GET', 'POST'] )
@login_required
def dashboard():
    username = current_user
    return render_template('dashboard.html', username=username)

@app.route('/logout', methods =[ 'GET', 'POST'] )
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/login', methods =[ 'GET', 'POST'] )
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)




@app.route('/register', methods =[ 'GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# @app.route('/logout')
# def logout():
#     return render_template('login.html')