import logging
import os
import random
import string

logger = logging.getLogger(__name__)

ALPHA_NUM = string.ascii_letters + string.digits


def generate_random_alphanum(length: int = 20) -> str:
    return "".join(random.choices(ALPHA_NUM, k=length))


def load_env_vars():
    if os.getenv("ENVIRONMENT") == "PRODUCTION":
        logger.info("Environment variables loaded from the environment")
    else:
        from dotenv import load_dotenv

        load_dotenv()
        logger.info("Environment variables loaded from the .env file")
