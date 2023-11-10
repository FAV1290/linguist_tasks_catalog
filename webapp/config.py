import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


SECRET_KEY = os.environ['TASKCAT_SECRET_KEY']
