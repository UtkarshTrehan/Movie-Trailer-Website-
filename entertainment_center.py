import media
from popular import get_movie_list
import fresh_tomatoes

list_of_movies = list()
movies_list = get_movie_list()
print(movies_list)
for movie in movies_list:
    data = movies_list[movie]
    list_of_movies.append(media.Movie(data['title'],data['overview'],
                                      data['poster_path'],
                                      data['trailer']))
fresh_tomatoes.open_movies_page(list_of_movies)

