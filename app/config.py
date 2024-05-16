from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_PASSWD")
DB_USER = os.environ.get("DB_HOST")
DB_PASS = os.environ.get("DB_PORT")
TOKEN_BOT = os.environ.get("TOKEN_BOT")
