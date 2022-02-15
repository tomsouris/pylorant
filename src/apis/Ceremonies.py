from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import CeremoniesModel

class Ceremonies(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url

    def all(self):
        url      = UrlBuilder.url(self.base_url, "/ceremonies")
        response = BaseRequest.get(self, url)
        model    = CeremoniesModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/ceremonies/{uuid}")
        response = self.get(url)
        model    = CeremoniesModel

        return Validator.Validate(model=model, response=response)