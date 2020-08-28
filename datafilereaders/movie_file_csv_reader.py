import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                movie = Movie(row["Title"], int(row["Year"]))
                director = Director(row["Director"])
                actors = row["Actors"].split(",")
                genres = row["Genre"].split(",")

                if movie not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(movie)

                if director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(director)

                for i in actors:
                    actor = Actor(i)
                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor)

                for i in genres:
                    genre = Genre(i)
                    if genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre)


