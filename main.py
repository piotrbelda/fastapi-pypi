import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles
from pathlib import Path
from data import db_session

from views import home, account, packages

app = fastapi.FastAPI() #docs_url=None, redoc_url=None

def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000)

def configure(dev_mode: bool = False):
    configure_routes()
    configure_templates()
    configure_db(dev_mode)

def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)

def configure_templates():
    fastapi_chameleon.global_init('templates')

def configure_db(dev_mode: bool = False):
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())

if __name__ == "__main__":
    main()
else:
    configure()