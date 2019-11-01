import pymongo


myclient = pymongo.MongoClient(
    "mongodb://172.31.18.96:27017,172.31.40.127:27017,172.31.27.254:27017/admin?replicaSet=myReplication")
mydb = myclient["MyChatDb"]
mycol = mydb["MyTable"]
while(1):
    print("Primary server is",myclient.address)
    print("Please, write your message")
    m = input()

    querry = {"message": m}
    mycol.insert_one(querry)

    for x in mycol.find():
        print(x)
