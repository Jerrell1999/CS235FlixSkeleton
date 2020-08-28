from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watchlist = []
        self.__index = 0

    def add_movie(self, movie: Movie):
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        try:
            return self.__watchlist[index]
        except:
            return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.__watchlist == []:
            return None
        else:
            return self.__watchlist[0]

    def __iter__(self):
        return iter(self.__watchlist)

    def __next__(self):
        if self.__index < len(self.__watchlist):
            self.__index += 1
            return self.select_movie_to_watch(self.__index-1)
        else:
            raise StopIteration
