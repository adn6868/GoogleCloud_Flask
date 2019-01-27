from pageRender import *
from flask import Flask, render_template, url_for
app = Flask(__name__)
# from app import routes

@app.route('/')
@app.route('/static' , methods = ['GET','POST'])



def index():
	pageRender = PageRender("one-piece-chap930")
	htmlRender = pageRender.render()

	user = {'username': 'Anh Nguyen'}
	name = 'One Piece - Chap 930'
	page = 1
	return render_template('index.html',title=name, htmlRender = htmlRender)
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)

