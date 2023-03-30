
import pymongo
import config

def mongo_insertone(DB, Col, item, loop = 0):
    myclient = pymongo.MongoClient(config.mango)
    mydb = myclient[DB]
    mycol = mydb[Col]
    if loop > 0:
        for r in range(len(item)):
            x = mycol.insert_one(item[r])
        return x 
    return mycol.insert_one(item)
