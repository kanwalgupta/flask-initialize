import os
from dotenv import load_dotenv

load_dotenv()

DATABASE=os.getenv('DB_NAME')
TEST_DATABASE = os.getenv('TEST_DB_NAME')
USER = os.getenv('USER_PG')
PASSWORD = os.getenv('PASSWORD_PG')

