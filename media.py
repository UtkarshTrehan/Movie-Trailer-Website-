# Creating a template (class Movie) for each thumbnail in the web page
import webbrowser


class Movie:
    ''' Movie template which correspond to each thumbnail shown on the web-page '''

    def __init__(self, movie_title, movie_storyline, movie_poster_image,movie_trailer):
        '''
        :param movie_title: contains the name of the movie
        :param movie_storyline: contains the Overview of the movie
        :param movie_poster_image: contains the link to the poster image of a movie
        :param movie_trailer: contains a link for youtube trailer for a movie
        '''

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer

    # This opens the movie trailer of the current instance
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

