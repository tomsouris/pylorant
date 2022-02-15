from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import SeasonsModel, CompetitiveSeasonsModel

class Seasons(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url
        
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/seasons")
        response = BaseRequest.get(self, url)
        model    = SeasonsModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/seasons/{uuid}")
        response = self.get(url)
        model    = SeasonsModel

        return Validator.Validate(model=model, response=response)

    def competitive_all(self):
        url      = UrlBuilder.url(self.base_url, "/seasons/competitive")
        response = BaseRequest.get(self, url)
        model    = CompetitiveSeasonsModel

        return Validator.Validate(model=model, response=response)

    def competitive_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url,  f"/seasons/competitive/{uuid}")
        response = BaseRequest.get(self, url)
        model    = CompetitiveSeasonsModel

        return Validator.Validate(model=model, response=response)