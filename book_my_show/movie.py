from typing import Dict
import uuid
from singleton import singleton


class Movie:
    def __init__(
        self, name: str, genre: str, length: int, language: str, resolution: str
    ):
        self.movie_id = uuid.uuid4()
        self.name = name
        self.genre = genre
        self.length = length
        self.language = language
        self.resolution = resolution


@singleton
class MovieManager:
    def __init__(self):
        self.movie_id_to_movie_map: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie):
        if movie.movie_id in self.movie_id_to_movie_map:
            raise Exception(f"Movie with id: {movie.movie_id} already exists")
        self.movie_id_to_movie_map[movie.movie_id] = movie

    def remove_movie(self, movie: Movie):
        if movie.movie_id not in self.movie_id_to_movie_map:
            raise Exception(f"Movie with id: {movie.movie_id} does not exist")
        self.movie_id_to_movie_map.pop(movie.movie_id)
