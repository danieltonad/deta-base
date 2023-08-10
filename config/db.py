from deta import Deta  # Import Deta

# Initialize
deta = Deta()

# This how to connect to or create a database.
database = deta.Base("simple_db")