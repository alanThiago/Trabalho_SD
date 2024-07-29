from pymongo import MongoClient
from pymongo.results import InsertOneResult, DeleteResult
from typing import List, Optional, Dict

from .constants import DB_NAME, COLLECTION_NAME
from .models import Movie

class MovieDAO:
    def __init__(self, uri: str):
        self.clientDB: MongoClient = MongoClient(uri)
        self.db = self.clientDB[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def add_movie(self, movie: Movie) -> str:
        result: InsertOneResult = self.collection.insert_one(movie.to_dict())
        return str(result.inserted_id)

    def get_movie(self, title: str) -> Optional[Dict]:
        data = self.collection.find_one({'title': title})
        if data:
            return data
        return None

    def get_all_movies(self) -> List[str]:
        movies: List[str] = []
        for doc in self.collection.find():
            movies.append(doc['title'])
        return movies


    def delete_movie(self, title: str) -> int:
        result: DeleteResult = self.collection.delete_one({'title': title})
        return result.deleted_count
