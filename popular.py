import urllib
import json
api_key = "ccaf78fee87c9c31d0a883dca9c71a69"
def get_movie_list():
    connection = urllib.urlopen("https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&page=1"
                                .format(api_key))
    output = connection.read()
    info = json.loads(str(output))
    movies_dict = dict()
    for movie in info['results']:
        trailer_link = youtube_link(movie['id'])
        movie_dict = {movie['title']: {'poster_path': "https://image.tmdb.org/t/p/w500/{}".format(movie['poster_path']),
                                       'overview': movie['overview'],
                                       'title': movie['title'],
                                       'trailer' : trailer_link}}
        movies_dict.update(movie_dict)
    connection.close()
    return movies_dict

def youtube_link(key):
    connection = urllib.urlopen("https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US"
                                .format(key,api_key))
    output = connection.read()
    info = json.loads(str(output))
    temp = info['results']
    key_link = temp[0]['key']
    return ("https://www.youtube.com/watch?v={}".format(key_link))