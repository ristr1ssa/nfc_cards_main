from flask import Flask, render_template
from database import get_data

app = Flask(__name__)


@app.route('/pages/None')
def NoneErrorHandler():
    return "Эта страница пока что не существует😭"


@app.route('/pages/<user_hash>')
def home(user_hash: str):
    data = get_data(user_hash=user_hash)[0]
    return render_template('home.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
