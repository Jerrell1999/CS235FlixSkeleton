from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self, username: str, password: str):
        self.__username = username.strip().lower()
        self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if type(other) is User:
            return self.__username == other.__username
        return False

    def __lt__(self, other):
        if self.__username < other.__username:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__username)

    def watch_movie(self, movie: Movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        self.__reviews.append(review)
