from proj.tasks import add, json_dump, insert_data_to_db
import json
from pymongo import MongoClient
# client = MongoClient("mongodb://root:rootpassword@localhost:27017?retryWrites=true&writeConcern=majority")
# # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = client["local"]
# mycol = mydb["employees"]
# from collections import dataclass

d = [
{ "name": "Chris", "age": 23, "city": "New York" },
{ "name": "Emily", "age": 19, "city": "Atlanta" },
{ "name": "Joe", "age": 32, "city": "New York" },
{ "name": "Kevin", "age": 19, "city": "Atlanta" },
{ "name": "Michelle", "age": 27, "city": "Los Angeles" },
{ "name": "Robert", "age": 45, "city": "Manhattan" },
{ "name": "Sarah", "age": 31, "city": "New York" }
]

for rec in d:
    # result = json_dump.delay(rec)
    insert_data_to_db.delay(rec)
#delay() is used to call a task
    # print(result.acknowledged())
#ready() returns whether the task has finished processing or not.
    # print(result.get(timeout=1))
#get() is used for getting results
# result.get(propagate=False)
#In case the task raised an exception, get() will re-raise the exception, but you can override this by specifying the propagate argument



# from pymongo import MongoClient

# client = MongoClient("mongodb://root:rootpassword@localhost:27017?retryWrites=true")
# # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = client["local"]
# mycol = mydb["employees"]

# # mydict = { "name": "John", "address": "Highway 37" }
# for rec in d:
#     mycol.insert_one(rec)