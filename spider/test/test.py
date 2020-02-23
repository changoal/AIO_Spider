import time

import pymongo

client = pymongo.MongoClient('192.168.154.131', 27017)
db = client['spider']
collection = db['test']


def test_mongo():
    data = {'aa': 'aaa'}
    res = collection.insert_one(data)
    print(res)
    client.close()


# test_mongo()

if __name__ == '__main__':
    # t = ''
    t = '2020-02-22 18:00:07'
    # print(time.mktime(time.strptime(t, "%Y-%b-%d %H:%M:%S")))
    d = time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S"))
    print(d*1000)
