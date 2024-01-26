import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Replace the placeholder with your Atlas connection string
url = os.environ.get("URL")

# Create a new client and connect to the server
client = MongoClient(url)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get database
mydb = client[os.environ.get("DB")]
# Get collection
mycol = mydb[os.environ.get("COLLECTION")]


def get_all_types():
    all_types = mycol.distinct("TYPE")
    return all_types


def get_sample():
    sample_query = [{"$sample": {"size": 12}}]
    return mycol.aggregate(sample_query)


def get_types_combination(ty1, ty2=None):
    project = {"_id": 0, "NAME": 1, "TYPE": 1, "POKEID": 1, "ICONS": 1}
    if ty2 is None:
        one_type_query = {"$and": [{"TYPE": f"{ty1}"}, {"TYPE": {"$size": 1}}]}
        return mycol.find(one_type_query, project)
    else:
        two_type_query = {"$and": [{"TYPE": {"$all": [f"{ty1}", f"{ty2}"]}}, {"TYPE": {"$size": 2}}]}
        return mycol.find(two_type_query, project)