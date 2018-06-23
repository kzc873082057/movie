# _*_coding:utf-8_*
from . import admin
from flask import render_template,redirect,url_for

@admin.route('/')
def index():
    return " this is andmin"

@admin.route('/login/')
def login():
    return render_template('admin/login.html')

@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))