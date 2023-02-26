from flask import Flask, render_template
from database import (configure_profile)

app = Flask(__name__, static_folder="static")


@app.route('/pages/None')
def NoneErrorHandler():
    return "Эта страница пока что не существует😭"


@app.route('/pages/<user_hash>')
def home(user_hash: str):
    profile = configure_profile(user_hash)
    return render_template('home.html', data=profile)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
