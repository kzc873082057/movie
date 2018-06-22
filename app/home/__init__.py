# _*_coding:utf-8_*
from flask import Blueprint

home = Blueprint("home", __name__)
import app.home.views
