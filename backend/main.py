"""
Точка входа в backend
"""
#
import sys
from core.create_base_app import create_base_app

from routing.books import router as books_routing
from core.config import configs


app = create_base_app(configs)

app.include_router(routers, prefix=configs.API)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8007)
    # uvicorn.run("main:app", host="localhost", port=8000, reload=True)
