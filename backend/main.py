"""
Точка входа в backend
"""
#
import sys
from core.create_base_app import create_base_app
sys.path.append('..\python_template')


from app.api import routers
from app.core.config import configs
from app.core.middlewares import ActionLoggingMiddleware
from app.core.container import Container

container = Container()
db = container.db()

app = create_base_app(configs)

app.include_router(routers, prefix=configs.API)
app.add_middleware(ActionLoggingMiddleware)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8007)
    # uvicorn.run("main:app", host="localhost", port=8000, reload=True)
