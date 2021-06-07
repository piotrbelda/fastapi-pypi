from viewmodels.shared.viewmodel import ViewModelBase
from starlette.requests import Request
from typing import List
from services import package_service, user_service
from data.package import Package

class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.release_count: int = 0
        self.user_count: int = 0
        self.package_count: int = 0
        self.packages: List = []

    async def load(self):
        self.release_count: int = await package_service.release_count()
        self.user_count: int = await user_service.user_count()
        self.package_count: int = await package_service.package_count()
        self.packages: List[Package] = await package_service.latest_packages(limit=7)

        '''{'package_count': 274_000,
         'release_count': 2_234_847,
         'user_count': 73_874,
         'packages': [
             {'id': 'fastapi', 'summary': "A great web framework"},
             {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
             {'id': 'httpx', 'summary': "Request for an async world!"}
         ]}'''