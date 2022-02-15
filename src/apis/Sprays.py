from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import SprayModel, SprayLevelModel

class Sprays(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url
        
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/sprays")
        response = BaseRequest.get(self, url)
        model    = SprayModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/sprays/{uuid}")
        response = self.get(url)
        model    = SprayLevelModel

        return Validator.Validate(model=model, response=response)

    def levels_all(self):
        url      = UrlBuilder.url(self.base_url, "/sprays/levels")
        response = BaseRequest.get(self, url)
        model    = SprayModel

        return Validator.Validate(model=model, response=response)
    
    def levels_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/sprays/levels/{uuid}")
        response = self.get(url)
        model    = SprayLevelModel

        return Validator.Validate(model=model, response=response)