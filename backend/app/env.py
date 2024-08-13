import os
from dotenv.main import load_dotenv

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

MAL_API_URL = os.getenv("MAL_API_URL")
MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")

MAL_API_HEADERS = {"X-MAL-CLIENT-ID": MAL_CLIENT_ID}
