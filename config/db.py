from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize
deta = Deta()

# This how to connect to or create a database.
database = deta.Base("simple_db")

# set key
database.project_key = os.environ.get('project-key-jaybird-cl1')