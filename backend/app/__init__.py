from fastapi import FastAPI

from sqlmodel import SQLModel
from app.models import (
    User,
    Product,
    UserProduct,
    Sale
)

from app.configurations.database import engine

# Área de importação de rotas:
from app.routes import (
    users,
    accounts,
    products
)

"""
==========================================================================
 ➠ Backend of TokShop (https://github.com/RodrigoSiliunas/)
 ➠ Section By: Rodrigo Siliunas (Rô: https://github.com/RodrigoSiliunas)
 ➠ Related system: Core of Aplication
==========================================================================
"""

app = FastAPI()


# Lógica para inicialização do nosso banco de dados;
# TODO: Fazer a verificação, caso as tabelas já estejam criadas não tentar criar novamente.
SQLModel.metadata.create_all(engine)


# Registro das minhas rotas:
app.include_router(users)
app.include_router(products)
app.include_router(accounts)
