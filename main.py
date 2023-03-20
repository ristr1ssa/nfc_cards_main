from flask import Flask, render_template
from database import (configure_profile)

app = Flask(__name__, static_folder="static")


@app.route('/')
def start():
    return render_template('start.html')

@app.route('/p/<user_hash>')
def home(user_hash: str):
    try:
        profile = configure_profile(user_hash)
    except Exception:
        return render_template('error.html')
    return render_template('home.html', data=profile)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1010', debug=False)
