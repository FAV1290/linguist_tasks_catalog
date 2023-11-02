import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


SECRET_KEY = os.environ['LINGUIST_TASKS_CATALOG_SECRET_KEY']
DB_HOST = os.environ['LINGUIST_TASKS_CATALOG_DB_HOST']
