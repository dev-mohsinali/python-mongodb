from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['movies']
movies_collection = db['movies']

# movies_data = [
#    {"movie_name": "High Life (2019)", "movie_director": "Claire Denis", "movie_starring": ['Robert Pattinson', 'Juliette Binoche', 'Mia Goth']},
#    {"movie_name": "Snowpiercer (2013)", "movie_director": "Bong Joon Ho", "movie_starring": ['Chris Evans', 'Tilda Swinton', 'Song Kang-Ho']},
#    {"movie_name": "District 9 (2009)", "movie_director": "Neill Blomkamp", "movie_starring": ['Sharlto Copley', 'David James']},
#    {"movie_name": "The Abyss (1989)", "movie_director": "Alfonso Cuaron", "movie_starring": ['Ed Harris', 'Mary Elizabeth Mastrantonio','Michael Biehn']},
#    {"movie_name": "Children Of Men (2006)", "movie_director": "Claire Denis", "movie_starring": ['Clive Owen', 'Julianne Moore', 'Clare-Hope Ashitey']}
# ]

# movies_collection.insert_many(movies_data)

#reading
for movie in movies_collection.find({"movie_name" : {'$regex' : "Snowpiercer"}}).limit(2):
   print(movie)