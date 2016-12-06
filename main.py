'''
main:
    Entry point for a basic web application, using the popular Flask
    framework for Python.

author: Abe Ratnofsky
'''

from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

# Route static files to their own folder
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Homepage
@app.route('/', methods=['GET'])
def hello():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
