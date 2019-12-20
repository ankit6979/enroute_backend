import pymongo

myclient = pymongo.MongoClient()
mydb = myclient["CentralEntertainment"]
mycol = mydb["item"]

def saveData(language, genre, name, url):
   base_document = {"_id": 1, "lang": {"hindi": {"sports": {}, "entertainment": {}, "documentry": {}, "news": {}}, "english": {"sports": {}, "entertainment": {}, "documentry": {}, "news": {}}}}

   if mycol.estimated_document_count() == 0:
      resp = mycol.insert_one(base_document)
      resp = mycol.update_one({"_id" : 1 }, {"$set": {"lang." + language + "." + genre + "." + name : url}})
   else:
      resp = mycol.update_one({"_id" : 1 }, {"$set": {"lang." + language + "." + genre + "." + name : url}})
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
print(queryData())