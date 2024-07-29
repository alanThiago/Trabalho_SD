import os

DB_NAME = 'data'
COLLECTION_NAME = 'movies'

URI_DB1 = f"mongodb://{os.getenv('USERNAME_DB1')}:{os.getenv('PASSWORD_DB1')}@{os.getenv('HOST_DB1')}:{os.getenv('PORT_DB1')}/{os.getenv('DB_NAME')}?authSource=admin"

URI_DB2 = f"mongodb://{os.getenv('USERNAME_DB2')}:{os.getenv('PASSWORD_DB2')}@{os.getenv('HOST_DB2')}:{os.getenv('PORT_DB2')}/{os.getenv('DB_NAME')}?authSource=admin"
