import media
from popular import get_movie_list
import fresh_tomatoes

# Declaring list_of_movies to old instances of class media
list_of_movies = list()
# This function returns nested dictionary of popular movies
movies_list = get_movie_list()
# Looping through each movie / Key
for movie in movies_list:
    # Extraction attributes of movie
    data = movies_list[movie]
    # Creating list of instance of class media
    list_of_movies.append(media.Movie(data['title'],
                                      data['overview'],
                                      data['poster_path'],
                                      data['trailer']))
# fresh_tomatoes take a list of media object to display the web page
fresh_tomatoes.open_movies_page(list_of_movies)
