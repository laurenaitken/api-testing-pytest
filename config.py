# Load BASE_URL from .env

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL is not set. Add it to your .env file. Copy .env.example to .env.")
