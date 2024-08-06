from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/login', methods=['GET', 'POST'])

def login( ):
    # data = request.form
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            flash(f'Account created for {firstname}', category='success')

                                     
    return render_template("login.html")

@auth.route('/logout')
def logout( ):
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up( ):
    return render_template("sign_up.html") 