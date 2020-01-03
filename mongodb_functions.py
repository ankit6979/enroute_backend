import os
import pymongo

user = os.environ['USER']
passwd = os.environ['PASS']

myclient = pymongo.MongoClient("mongodb+srv://" + user + ":" + passwd +
                               "@cluster0-kfqgc.mongodb.net/CentralEntertainment?retryWrites=true&w=majority")
mydb = myclient["CentralEntertainment"]
mycol = mydb["item"]
id=17

def getMediaDetails(media_id):
    resps = mydb['MediaObject'].find({"_id":media_id})
    return [resp for resp in resps]

def getCoordinates(pnr):
    resp = mydb["Map"].find_one({"PNR": pnr}, {"_id": 0})
    return resp


def AddContent(pnr, media_id, viewflag, likeflag, comments, anonymousflag):
    if(anonymousflag):
        pnr = "Anonymous"
    returnVal = mydb['MediaObject'].update_one({"_id": media_id}, {"$inc": {"Likes": likeflag, "Views": viewflag}, "$push": {
                                               "Viewers": pnr, "PeopleLiked": pnr, "Comments": {"pnr": pnr, "comments": comments}}})
    return {"result": returnVal.matched_count > 0}


def getContent(pnr):
    languages = mydb['UserData'].find({"PNR": pnr}, {"_id": 0, "Lang_pref": 1})
    genres = mydb['UserData'].find({"PNR": pnr}, {"_id": 0, "Genre_pref": 1})
    # mediaObjects = []
    for lang in languages:
        templang = lang['Lang_pref']
    for gen in genres:
        tempgen = gen['Genre_pref']
    language = templang
    genres = tempgen
    resp = []
    for genre in genres:
        resps = mydb['MediaObject'].aggregate([{
            "$match": {
                "$and": [
                    {"Language": {"$in": language}},
                    {"Genre": genre}
                ]
            }
        },
            {"$limit": 2}
        ])
        for content in resps:
            resp.append(content)

    return [respt for respt in resp]


def userPreference(pnr, name, lang_pref, genre_pref):
    val = mydb['UserData'].update_one({"PNR": pnr, "Name": name}, {
                                      "$set": {"Lang_pref": lang_pref, "Genre_pref": genre_pref}})
    return {"result": val.matched_count > 0}


def checkUser(pnr, name, seatno):
    returnVal = mydb['UserCredential'].find(
        {"Name": name, "PNR": pnr, "SeatNo": seatno}).count() > 0
    return {"result": returnVal}


def saveData(language, genre, name, url, description, thumbnailurl):
    global id
    id += 1
    resp = mydb['MediaObject'].insert({"_id": id, "Name": name, "Language": language, "Genre": genre, "url": url, "Views": 0, "Viewers": [
    ], "Likes": 0, "PeopleLiked": [], "Comments": [{}], "Description": description, "ThumbnailUrl": thumbnailurl})
    print("saved")
    return resp


def deleteData(language, genre, name):
    resp = mycol.update_one(
        {"_id": 1}, {"$unset": {"lang." + language + "." + genre + "." + name: 1}})
    print("deleted")
    return resp


def queryData(language=None, genre=None):
    language = None
    video_list = []
    if language == None:
        resp = mycol.find_one({"_id": 1}, {"_id": 0})
        lang = resp['lang']
        for i, j in lang.items():
            for x, y in j.items():
                for a, b in y.items():
                    d = {}
                    d['name'] = a
                    d['url'] = b
                    video_list.append(d)

    # elif (language != None) & (genre == None):
    #    resp = mycol.find_one({"_id" : 1}, {"_id" : 0,  "lang" + "." + language : 1})
    # elif (language != None) & (genre != None):
    #    resp = mycol.find_one({"_id" : 1}, {"_id" : 0,  "lang" + "." + language + "." + genre : 1})
    return video_list


def queryLanguage(language):
    resps = mydb['MediaObject'].find({"Language": language}, {
                                     "_id": 1, "Name": 1, "Genre": 1, "url": 1, "ThumbnailUrl": 1, "Description":1})
    return [resp for resp in resps]


def queryGenre(genre):
    resps = mydb['MediaObject'].find(
        {"Genre": genre}, {"_id": 1, "Name": 1, "url": 1, "ThumbnailUrl": 1, "Description":1})
    return [resp for resp in resps]

#docs = getContent("1024586167")
#print([doc for doc in docs])
