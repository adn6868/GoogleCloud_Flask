# from flask import Flask
from flask import Flask, render_template, url_for
app = Flask(__name__)
# from app import routes

@app.route('/')
@app.route('/static' , methods = ['GET','POST'])

def index():
    user = {'username': 'Anh Nguyen'}
    page = 1
    return render_template('index.html')
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)