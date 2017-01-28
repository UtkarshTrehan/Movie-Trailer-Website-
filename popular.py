import urllib
import json


def get_movie_list():

    api_key = "ccaf78fee87c9c31d0a883dca9c71a69"

    connection = urllib.urlopen("https://api.themoviedb.org/3/movie/top_rated?api_key={}"
                                "&language=en-US&page=1".format(api_key))

    output = connection.read()
    movies_dict = dict()
    movie_dict = dict()
    info = json.loads(str(output))

    for movie in info['results']:
        movie_dict = {movie['title']: {'poster_path': movie['poster_path'],
                                       'overview': movie['overview'],
                                       'title': movie['title']}}
        movies_dict.update(movie_dict)
    connection.close()
    return movies_dict
