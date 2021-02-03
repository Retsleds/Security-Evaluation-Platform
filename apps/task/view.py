from flask import Blueprint, request, Response, render_template, redirect, url_for
from apps.extensions import mongo
from bson.objectid import ObjectId


task_bp = Blueprint('task', __name__)

# @task_bp.route('/task', methods=['GET', 'POST'], endpoint='dashboard')
# def dashboard():
#     if request.cookies.get('uid'):
#         user = mongo.db.users.find_one({'_id':ObjectId(request.cookies.get('uid'))})
#         companyList = mongo.db.companies.find()
#         return render_template('dashboard.html', user=user, companyList=companyList)
#     return render_template('dashboard.html')


@task_bp.route('/showtask', methods=['GET', 'POST'], endpoint='showtask')
def showtask():
    companyList = mongo.db.companies.find()
    return render_template('task.html', companyList=companyList)

@task_bp.route('/createcompany', methods=['GET', 'POST'], endpoint='createcompany')
def createcomany():
    ename = request.form.get('ename')
    econtact = request.form.get('econtact')
    companies_collection = mongo.db.companies
    companies_collection.insert({'ename': ename, 'econtact':econtact})
    return redirect(url_for('task.showtask'))

@task_bp.route('/delcompany', methods=['GET', 'POST'], endpoint='delcompany')
def delcompany():
    pass
    # TODO


