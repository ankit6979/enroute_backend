import pymongo

myclient = pymongo.MongoClient("")
mydb = myclient["CentralEntertainment"]
mycol = mydb["Map"]

docs = [{
    "_id": 1,
    "Name": "ZNMD",
    "Language": "Hindi",
    "Genre": "Travel",
    "url": "C://movies",
    "Views": 3,
    "Viewers": [
        "1024",
        "1024",
        "Anonymous"
    ],
    "Likes": 0,
    "PeopleLiked": [
        "1024",
        "1024",
        "Anonymous"
    ],
    "Comments": [
        {
            "pnr": "1024",
            "comment": "Awesome"
        },
        {
            "pnr": "Anonymous",
            "comment": "Awesome"
        }
    ],
    "Description": "Story of life",
    "ThumbnailUrl": "C://Thumbnails"
},
{
    "_id": 2,
    "Name": "Jhonny English",
    "Language": "English",
    "Genre": "Comedy",
    "url": "C://movies/english",
    "Views": 4,
    "Viewers": [
        "1024",
        "Anonymous",
        "Anonymous",
        "1524"
    ],
    "Likes": 3,
    "PeopleLiked": [
        "Anonymous",
        "Anonymous",
        "1524"
    ],
    "Comments": [
        {
            "pnr": "1524",
            "comment": "Loved it"
        },
        {
            "pnr": "1024",
            "comment": "Best acting"
        }
    ],
    "Description": "Relive your childhood",
    "ThumbnailUrl": "C://Thumbnails/english/comedy"
},
{
    "_id": 3,
    "Name": "Koi mil gaya",
    "Language": "Hindi",
    "Genre": "Comedy",
    "url": "C://movies/comedy",
    "Views": 1,
    "Viewers": [
        "1524"
    ],
    "Likes": 1,
    "PeopleLiked": [
        "1524"
    ],
    "Comments": [
        {
            "pnr": "1524",
            "comment": "Time pass"
        }
    ],
    "Description": "Jadoo",
    "ThumbnailUrl": "C:\\Thumbnailshindi"
},
{
    "_id": 4,
    "Name": "Avengers",
    "Language": "English",
    "Genre": "Action",
    "url": "C://movies/english",
    "Views": 1,
    "Viewers": [
        "1024"
    ],
    "Likes": 1,
    "PeopleLiked": [
        "1024"
    ],
    "Comments": [
        {
            "pnr": "1024",
            "comment": "Loved it"
        }
    ],
    "Description": "Superheroes of earth",
    "ThumbnailUrl": "C://Thumbnails/english/action"
},
{
    "_id": 5,
    "Name": "Annabelle",
    "Language": "English",
    "Genre": "Horror",
    "url": "C://movies/english",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "Miss me",
    "ThumbnailUrl": "C://thumbnail"
},
{
    "_id": 6,
    "Name": "Bhootnath",
    "Language": "Hindi",
    "Genre": "Horror",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "friendly ghost",
    "ThumbnailUrl": "C://Thumbnails/hindi/horror"
},
{
    "_id": 7,
    "Name": "YJHD",
    "Language": "Hindi",
    "Genre": "Travel",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "Follow passion",
    "ThumbnailUrl": "C://Thumbnails/hindi/travel"
},
{
    "_id": 8,
    "Name": "Swadesh",
    "Language": "Hindi",
    "Genre": "Travel",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "shahrukh time",
    "ThumbnailUrl": "C://Thumbnails/hindi/horror"
},
{
    "_id": 9,
    "Name": "Dhol",
    "Language": "Hindi",
    "Genre": "Comedy",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "best comedy",
    "ThumbnailUrl": "C://Thumbnails/hindi/comedy"
},
{
    "_id": 10,
    "Name": "Golmaal",
    "Language": "Hindi",
    "Genre": "Comedy",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "slient",
    "ThumbnailUrl": "C://Thumbnails/hindi/comedy"
},
{
    "_id": 11,
    "Name": "Krishna cottage",
    "Language": "Hindi",
    "Genre": "Horror",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "Really scary",
    "ThumbnailUrl": "C://Thumbnails/hindi/horror"
},
{
    "_id": 12,
    "Name": "Stree",
    "Language": "Hindi",
    "Genre": "Horror",
    "url": "C://movies/hindi",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "latest horror",
    "ThumbnailUrl": "C://Thumbnails/hindi/horror"
},
{
    "_id": 13,
    "Name": "Conjuring",
    "Language": "English",
    "Genre": "Horror",
    "url": "C://movies/english",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "scary as hell",
    "ThumbnailUrl": "C://Thumbnails/english/horror"
},
{
    "_id": 14,
    "Name": "Insidious",
    "Language": "English",
    "Genre": "Horror",
    "url": "C://movies/english",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "",
    "ThumbnailUrl": "C://Thumbnails/english/horror"
},
{
    "_id": 15,
    "Name": "Mr Bean",
    "Language": "English",
    "Genre": "Comedy",
    "url": "C://movies/english",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "very funny",
    "ThumbnailUrl": "C://Thumbnails/english/comedy"
},
{
    "_id": 16,
    "Name": "Now you see me",
    "Language": "English",
    "Genre": "Action",
    "url": "C://movies/english",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "interesting movie",
    "ThumbnailUrl": "C://Thumbnails/english/action"
},
{
    "_id": 17,
    "Name": "Batman",
    "Language": "English",
    "Genre": "Action",
    "url": "C://movies/english",
    "Views": 0,
    "Viewers": [],
    "Likes": 0,
    "PeopleLiked": [],
    "Comments": [
        {}
    ],
    "Description": "Best of DC",
    "ThumbnailUrl": "C://Thumbnails/english/action"
}]

#mycol.insert(docs)
 
mapData = [{
    "PNR" : "1024586167",
    "Source" : "",
    "Destination" : "",
    "SourceLat" : "",
    "SourceLong" : "",
    "DestinationLat" : "",
    "DestinationLong" : ""
}
,
{
    "PNR" : "1254867092",
    "Source" : "",
    "Destination" : "",
    "SourceLat" : "",
    "SourceLong" : "",
    "DestinationLat" : "",
    "DestinationLong" : ""
}
,
{
    "PNR" : "1394456078",
    "Source" : "",
    "Destination" : "",
    "SourceLat" : "",
    "SourceLong" : "",
    "DestinationLat" : "",
    "DestinationLong" : ""
}
,
{
    "PNR" : "1680763147",
    "Source" : "",
    "Destination" : "",
    "SourceLat" : "",
    "SourceLong" : "",
    "DestinationLat" : "",
    "DestinationLong" : ""
}
,
{
    "PNR" : "8600400135",
    "Source" : "",
    "Destination" : "",
    "SourceLat" : "",
    "SourceLong" : "",
    "DestinationLat" : "",
    "DestinationLong" : ""
}
,
{
    "PNR" : "4554799786",
    "Source" : "",
    "Destination" : "",
    "SourceLat" : "",
    "SourceLong" : "",
    "DestinationLat" : "",
    "DestinationLong" : ""
}]
mycol.insert(mapData)