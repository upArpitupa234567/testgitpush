import pymongo

# from pymongo.mongo_client import MongoClient

client = pymongo.MongoClient("mongodb+srv://arpitupadhyay382:Arpit1234@cluster0.kc3lbkq.mongodb.net/?retryWrites=true&w=majority")  # here we are connecting mongodb with pycharm

db = client.test
print(db)

d = {
    "name" : "sudhanshu",
    "email": "arpitupadhyay958@gmail.com",
    "surname": "upadhyay"
}

db1 = client['mongoTest']
coll = db1['test']
coll.insert_one(d)