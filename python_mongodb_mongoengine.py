import mongoengine as db
from app_constants import constants

db.connect(constants.db, host='localhost', port=27017)

#favourite movies collection
class Movies(db.Document):
    movie_name = db.StringField()
    movie_director = db.StringField()
    movie_starring = db.ListField()

    def to_json(self):
        return {
            'movie_name':self.movie_name,
            'movie_director':self.movie_director,
            'movie_starring':self.movie_starring
        }

#movie = Movies(movie_name='Silent Running (1972)', movie_director='Douglas Trumbull', movie_starring= ['Bruce Dern','Cliff Potts']) 
#movie.save()

for movie in Movies.objects():
    print(movie.to_json())

#updating
#Movies.objects(movie_name='Silent Running (1972)').update_one(set__movie_name='Silent Running')

# Find movies 
searched_movie = Movies.objects(movie_name__contains='Run').only('movie_name').exclude('id')
print(searched_movie.to_json())

