from pymongo import MongoClient
# import request
from flask import Flask, render_template, url_for, request
app = Flask(__name__)
# from app import routes


# client = pymongo.MongoClient(
#     "mongodb+srv://anguyen:Emyeubacho1996!@cluster0-nghj0.gcp.mongodb.net/test?retryWrites=true")
# db = client.test
# print(db)


@app.route('/')
@app.route('/static', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['fullname']
    email = request.form['email']
    message = request.form['message']
    post = {'Name': name, 'Email': email, 'Message': message}
    client = MongoClient(
        "mongodb+srv://anguyen:Emyeubacho1996!@cluster0-nghj0.gcp.mongodb.net/test?retryWrites=true", ssl=True)

    db = client.messager
    collection = db.messager
    rec_id1 = collection.insert_one(post)
    print("Succesfully posted with id ", rec_id1)
    return render_template('thankyou.html')


# db = client.messager
# collection = db.messager


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082, debug=True)
