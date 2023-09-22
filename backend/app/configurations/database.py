from sqlmodel import create_engine

"""
==========================================================================
 ➠ Database Configuration File (https://github.com/RodrigoSiliunas/)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Database (PyMongo)
==========================================================================
"""

engine = create_engine("sqlite:///app/database/tokshop.db")
