import pymongo

client = pymongo.MongoClient('192.168.154.131', 27017)
db = client['spider']
collection = db['test']


def test_mongo():
    data = {'aa': 'aaa'}
    res = collection.insert_one(data)
    print(res)
    client.close()


test_mongo()
