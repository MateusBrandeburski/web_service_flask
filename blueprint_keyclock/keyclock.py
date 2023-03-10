from flask import Blueprint, request, render_template
from flask_login import login_user, logout_user, login_required, current_user

keyclock = Blueprint('keyclock', __name__)



@keyclock.route('/login', methods=['GET', 'POST'])
def login():
    pass