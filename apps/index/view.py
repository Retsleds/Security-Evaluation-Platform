from flask import Blueprint, request, Response, render_template,redirect, url_for
from apps.extensions import mongo
from bson.objectid import ObjectId

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods = ['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users_collection = mongo.db.users
        if users_collection.find_one({'username': username}):
            user = users_collection.find_one({'username': username})
            if user['password'] == password:
                response = redirect(url_for('index.dashboard'))
                response.set_cookie('uid', str(user['_id']), max_age=1800)
                return response
            else:
                msg = 'Password is not correct'
                return render_template('login.html', msg=msg)
        else:
            msg = 'No account exists'
            return render_template('login.html', msg=msg)

    return render_template('login.html')


@index_bp.route('/logout', endpoint='logout')
def logout():
    response = redirect(url_for('index.login'))
    response.delete_cookie('uid')
    return response


@index_bp.route('/task', methods=['GET', 'POST'], endpoint='dashboard')
def dashboard():
    if request.cookies.get('uid'):
        user = mongo.db.users.find_one({'_id':ObjectId(request.cookies.get('uid'))})

        return render_template('dashboard.html', user=user)
    return render_template('dashboard.html')



@index_bp.route('/test')
def test():
    return render_template('base_nav.html')