from .constants import URI_DB1, URI_DB2
from .dao import MovieDAO
from .models import Movie


db1 = MovieDAO(URI_DB1)
db2 = MovieDAO(URI_DB2)
