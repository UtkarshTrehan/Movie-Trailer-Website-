import urllib
import json

# api_key for "www.themoviedb.org" needed to generate requests
api_key = "ccaf78fee87c9c31d0a883dca9c71a69"
link1 = "https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&page=1"


def get_movie_list():
    '''link1 can be update (https://developers.themoviedb.org/3/movies)
       to get particular typ of response from server like
        Get Upcoming Movies
        Get Latest Movies
        Get Now Playing Movies
        Get Popular Movies
        Get Top Rated Movies

       Args: null

       Returns : Dictionary of Movies

     '''
    connection = urllib.urlopen(link1.format(api_key))
    output = connection.read()
    # storing .json response for list of now-playing movies
    info = json.loads(str(output))
    movies_dict = dict()
    # Fetching for attributes of all movies
    for movie in info['results']:
        trailer_link = youtube_link(movie['id'])
        movie_dict = {movie['title']: {'poster_path': "https://image.tmdb.org/t/p/w500/{}".format(movie['poster_path']),
                                       'overview': movie['overview'],
                                       'title': movie['title'],
                                       'trailer' : trailer_link}}
        movies_dict.update(movie_dict)
    connection.close()
    # Returning Dictionary with movie name as their Key and attributes as Values
    return movies_dict


# Fetches youtube link for the given id (key) for a particular movie
def youtube_link(key):
    """This function return a fully formatted youtube link for a particular id of movie

    Arg: id of a movie

    Return : Fully formatted youtube trailer link for given id

    """
    connection = urllib.urlopen("https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US"
                                .format(key,api_key))
    output = connection.read()
    # Storing json response
    info = json.loads(str(output))
    temp = info['results']
    # Finding the value of key name 'key'
    key_link = temp[0]['key']
    # Returning the youtube link with the following key for a particular movie id
    connection.close()
    return "https://www.youtube.com/watch?v={}".format(key_link)