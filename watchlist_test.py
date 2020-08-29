import pytest
from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList

@pytest.fixture()
def watchlist():
    return WatchList()

#Test the addition of a movie to the end of the watch list.
def test_add_movie(watchlist):
    assert watchlist.size() == 0
    watchlist.add_movie(Movie("Moana",2016))
    assert watchlist.size() == 1
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.size() == 2

#If a movie is already contained in the watch list, it is not added once again.
def test_add_same_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    assert watchlist.size() == 1
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert watchlist.size() == 2
    watchlist.add_movie(Movie("Moana", 2016))
    assert watchlist.size() == 2

#Test the removement of a movie from the watch list.
def test_remove_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    assert watchlist.size() == 1
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert watchlist.size() == 2
    watchlist.remove_movie(Movie("Moana", 2016))
    assert watchlist.size() == 1

#If a movie is not contained in the watch list, the remove() method does nothing.
def test_remove_movie_not_in_watchlist(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    assert watchlist.size() == 1
    watchlist.add_movie(Movie("Ice Age", 2002))
    assert watchlist.size() == 2
    watchlist.remove_movie(Movie("JoJo's Bizarre Adventure", 2014)) #YareYare Daze
    assert watchlist.size() == 2

#select_movie_to_watch() returns the movie with the index passed as a parameter to this function.
def test_select_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Final Fantasy VII: Advent Children", 2005))
    assert watchlist.size() == 2
    assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016)
    assert watchlist.select_movie_to_watch(1) == Movie("Final Fantasy VII: Advent Children", 2005)

#select_movie_to_watch() checks if the index is out of bounds. If this is the case, the method returns None.
def test_select_movie_fails(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("DotA2 is neat", 2000))
    watchlist.add_movie(Movie("League is trash", 2000))
    assert watchlist.size() == 3
    assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016)
    assert watchlist.select_movie_to_watch(2) == Movie("League is trash", 2000)
    assert watchlist.select_movie_to_watch(3) == None
    assert watchlist.select_movie_to_watch(-1) == None

#first_movie_in_watchlist() returns the movie which is the first in the watch list
def test_select_first(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("DotA2 is neat", 2000))
    watchlist.add_movie(Movie("League is trash", 2000))
    assert watchlist.size() == 3
    assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016)
    watchlist.remove_movie(Movie("Moana", 2016))
    assert watchlist.first_movie_in_watchlist() == Movie("DotA2 is neat", 2000)

#If the watch list is empty, it returns None
def test_select_first_from_empty_watchlist(watchlist):
    watchlist.add_movie(Movie("DotA2 is neat", 2000))
    watchlist.remove_movie(Movie("DotA2 is neat", 2000))
    assert watchlist.first_movie_in_watchlist() == None

#size() returns the number of movies in the watch list.
def test_size(watchlist):
    assert watchlist.size() == 0

def test_next_movie(watchlist):
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))

    iterator = iter(watchlist)
    assert next(iterator) == Movie("Moana", 2016)
    assert next(iterator) == Movie("Ice Age", 2002)
    assert next(iterator) == Movie("Guardians of the Galaxy", 2012)
