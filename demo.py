# coding=utf-8
# @Author: yiTian.zhang
# @LastEditors: yiTian.zhang
# @Date: 2022-12-19 17:09:51

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "1.0"


if __name__ == "__main__":
    app.run("0.0.0.0", 59999)
