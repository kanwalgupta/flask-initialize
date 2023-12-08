import os
from dotenv import load_dotenv

load_dotenv()

DATABASE=os.getenv('DB_NAME')
USER = os.getenv('USER_PG')
PASSWORD = os.getenv('PASSWORD_PG')