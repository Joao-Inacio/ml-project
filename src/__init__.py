import logging

import dagshub
from dotenv import load_dotenv

dagshub.init(repo_owner="Joao-Inacio", repo_name="ml-project")


load_dotenv()

# Configure the logging strategy
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)
