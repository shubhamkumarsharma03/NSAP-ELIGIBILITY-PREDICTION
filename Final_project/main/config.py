# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("API_KEY")
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")

if not API_KEY or not DEPLOYMENT_URL:
    raise ValueError("Missing API_KEY or DEPLOYMENT_URL in environment.")
