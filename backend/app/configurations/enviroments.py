from os import environ
from dotenv import load_dotenv

"""
==========================================================================
 ➠ Enviroments Configuration File (https://github.com/RodrigoSiliunas/)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Enviroments
==========================================================================
"""

load_dotenv()

ENCRYPTION_ALGORITHM = environ.get('ENCRYPTION_ALGORITHM')
SECRET_KEY = environ.get('JWT_SECRET_KEY')
ACCESS_TOKEN_EXPIRES = int(environ.get('JWT_ACCESS_TOKEN_EXPIRES'))
REFRESH_TOKEN_EXPIRES = int(environ.get('JWT_REFRESH_TOKEN_EXPIRES'))
