
from .celery_config import celery_app, client, MONGO_DB_NAME, MONGO_DB_COLLECTION
from bson import json_util
mydb = client[MONGO_DB_NAME]
mycol = mydb[MONGO_DB_COLLECTION]


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def json_dump(s):
    return s

@celery_app.task
def insert_data_to_db(rec):
    print("rec==>", rec)
    import bson
    
    result = mycol.insert_one(rec)
    return result.acknowledged
