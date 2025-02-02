from celery import Celery
from pymongo import MongoClient

celery_app = Celery('celeryapp', broker='pyamqp://guest@localhost//', 
backend="mongodb://root:rootpassword@localhost:27017", include=['proj.tasks'],
mongodb_backend_settings={
                 'database': 'local',
                 'taskmeta_collection': 'celery_tasks',
             })


client = MongoClient("mongodb://root:rootpassword@localhost:27017?retryWrites=true")
MONGO_DB_NAME = "local"
MONGO_DB_COLLECTION = "employees"

