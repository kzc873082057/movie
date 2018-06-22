# _*_coding:utf-8_*
from flask import Blueprint

admin = Blueprint("admin", __name__)
import app.admin.views
