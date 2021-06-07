from viewmodels.shared.viewmodel import ViewModelBase
from data.user import User
from starlette.requests import Request
from services import user_service

class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

    async def load(self):
        self.user = await user_service.get_user_by_id(self.user_id)