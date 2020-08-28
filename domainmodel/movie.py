from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, title: str, release_year: int):
        self.__title = title
        self.__release_year = release_year
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if new_title != "" and type(new_title) is str:
            self.__title = new_title.strip()

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, new_release_year: int):
        if new_release_year >= 1900:
            self.__release_year = new_release_year

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if type(new_description) is str:
            self.__description = new_description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, new_director):
        if type(new_director) is Director:
            self.__director = new_director

    @property
    def actors(self):
        return self.__actors

    @property
    def genres(self):
        return self.__genres

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime_minutes: int):
        if new_runtime_minutes >= 0:
            self.__runtime_minutes = new_runtime_minutes
        else:
            raise ValueError

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if self.__title == other.__title and self.__release_year == other.__release_year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        else:
            return self.__title < other.__title

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))

    def add_actor(self, actor):
        if type(actor) is Actor and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if type(actor) is Actor and actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) is Genre and genre not in self.__genres:
            self. __genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) is Genre and genre in self.__genres:
            self.__genres.remove(genre)


