from flask import Flask
app = Flask(__name__)

class banner:
	"""docstring for banner"""
	def __init__(self, arg):
		self.arg = arg
	def toString(self):
		return "I'm " + str(self.arg)

@app.route("/")
def hello():
	return "Hi!"

def main():
	# print (hello2())
	b = banner("Anh")
	b.toString()
	return b.toString()
# def hello2():
# 	return "sup"
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)