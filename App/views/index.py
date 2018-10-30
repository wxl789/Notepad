from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('indexBP',__name__)

@bp.route('/index/')
@login_required      #需要登录后才能访问的页面
def index():

    return render_template('index.html')