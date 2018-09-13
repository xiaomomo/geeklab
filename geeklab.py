from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('lab.html')


@app.route('/poem')
def poem():
    return render_template('poem.html')


@app.route('/composition')
def composition():
    return render_template('composition.html')


@app.route('/emotion')
def emotion():
    return render_template('emotion.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
