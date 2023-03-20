from flask import Blueprint, render_template, request, redirect, session, flash, url_for
import pyautogui

limpa_email = Blueprint('limpa_email', __name__, template_folder='templates')


@limpa_email.route('/limpa', methods=['GET'])
def index():
    
    print('tudo certo')
    pyautogui.sleep(3)
    print(pyautogui.position())
    return render_template('home/home.html')