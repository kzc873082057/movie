# _*_coding:utf-8_*
from . import admin


@admin.route("/")
def index():
    return "admin page"
