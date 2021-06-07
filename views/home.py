import fastapi
from fastapi_chameleon import template
from viewmodels.home.indexviewmodel import IndexViewModel
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()

@router.get("/")
@template(template_file='home/index.pt')
async def index(request: Request):
    vm = IndexViewModel(request)
    await vm.load()
    return vm.to_dict()

@router.get("/about")
@template(template_file='home/about.pt')
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()