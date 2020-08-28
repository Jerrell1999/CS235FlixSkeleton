from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text.strip()
        self.__timestamp = datetime.today()

        if 0 < rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None


    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, new_movie):
        if type(new_movie) is Movie:
            self.__movie = new_movie

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, new_review_text):
        if type(new_review_text) is str:
            self.__review_text = new_review_text.strip()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, new_rating):
        if type(new_rating) is int and 0 < new_rating <= 10:
            self.__rating = new_rating
        else:
            self.__rating = None

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        pass

    def __repr__(self):
        return f"Review :{self.__review_text}, {self.__timestamp}"

    def __eq__(self, other):
        if self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp:
            return True
        else:
            return False
