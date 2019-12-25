import pymongo

myclient = pymongo.MongoClient()
mydb = myclient["CentralEntertainment"]
mycol = mydb["MediaObject"]
id = 4

def AddContent(pnr, media_id, viewflag, likeflag, comments, anonymousflag):
   if(anonymousflag):
      pnr = "Anonymous"
   returnVal = mydb['MediaObject'].update_one({"_id":media_id}, {"$inc":{"Likes":likeflag, "Views":viewflag}, "$push":{"Viewers":pnr, "PeopleLiked":pnr, "Comments":{"pnr":pnr, "comments":comments}}})   
   return {"result": returnVal.matched_count>0}

def userPreference(pnr, name, lang_pref, genre_pref):
   val = mydb['UserData'].update_one({"PNR":pnr, "Name":name}, {"$set": {"Lang_pref":lang_pref, "Genre_pref":genre_pref}})
   return {"result":val.matched_count>0}

def checkUser(pnr, name, seatno):
   returnVal = mydb['UserCredential'].find({"Name":name, "PNR":pnr, "SeatNo":seatno}).count() > 0
   return {"result":returnVal}

def saveData(language, genre, name, url, description, thumbnailurl):
   global id
   id += 1
   resp = mydb['MediaObject'].insert({"_id":id, "Name":name, "Language":language, "Genre":genre, "url":url, "Views":0, "Viewers":[], "Likes":0, "PeopleLiked":[], "Comments":[{}],"Description":description, "ThumbnailUrl":thumbnailurl})
   print("saved")
   return resp 

def deleteData(language, genre, name):
   resp = mycol.update_one({"_id" : 1 }, {"$unset": {"lang." + language + "." + genre + "." + name : 1}})
   print("deleted")
   return resp

def queryData(language=None, genre=None):
   language=None
   video_list = []
   if language == None: 
      resp = mycol.find_one({"_id" : 1}, {"_id" : 0 })
      lang = resp['lang']
      for i, j in lang.items():
         for x,y in j.items():
            for a,b in y.items():
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
   resps = mydb['MediaObject'].find({"Language":language}, {"_id":1, "Name":1, "Genre":1, "url":1, "ThumbnailUrl":1 })
   return [resp for resp in resps]

def queryGenre(genre):
   resps = mydb['MediaObject'].find({"Genre":genre}, {"_id":1, "Name":1, "url":1, "ThumbnailUrl":1 })
   return [resp for resp in resps]

#docs = queryLanguage("English")
#print([doc for doc in docs])