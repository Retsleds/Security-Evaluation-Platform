from flask import Blueprint, request, Response, render_template,redirect, url_for
from apps.extensions import mongo
from bson.objectid import ObjectId

nmap_bp = Blueprint('nmap', __name__)

@nmap_bp.route('/nmap', methods = ['GET', 'POST'], endpoint='login')
def nmap():
    return render_template('nmap.html')