
import datetime
from pymongo import MongoClient

# client = MongoClient(
#     "mongodb+srv://anguyen:Emyeubacho1996!@cluster0-nghj0.gcp.mongodb.net/test?retryWrites=true")
# db = client.test
# print(db)

try:
    client = MongoClient("mongodb+srv://anguyen:Emyeubacho1996!@cluster0-nghj0.gcp.mongodb.net/test?retryWrites=true",
                         ssl=True)
    print("connected")
except:
    print('failed')


db = client.messager
collection = db.messager

print(collection)
# for i in collection.find():
#     print(i)
print(collection)
post1 = {
    "Name": "Alex",
    "Email": "alex@truman.edu",
    "Message": "You are awesome"
    # "date": datetime.datetime.utcnow()
}
# print(client.comic)
rec_id1 = collection.insert_one(post1)
print(rec_id1)
# post2 = {
#     "Name": "Bob",
#     "Email": "bob@truman.edu",
#     "Message": "You are not awesome",
#     "date": datetime.datetime.utcnow()
# }
# post3 = {
#     "Name": "Cindy",
#     "Email": "cindy@truman.edu",
#     "Message": "Maybe",
#     "date": datetime.datetime.utcnow()
# }

# collection = db.message


# rec_id1 = collection.insert_one(post1)
# rec_id2 = collection.insert_one(post2)
# rec_id3 = collection.insert_one(post3)

# print("Data inserted with record ids", rec_id1, " ", rec_id2, rec_id3)

# # Printing the data inserted
# cursor = collection.find()
# for record in cursor:
#     print(record)
