import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """Configuration class for Yougile API"""

    BASE_URL = "https://yougile.com/api-v2"
    API_KEY = os.getenv("YOUGILE_API_KEY", "")

    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
