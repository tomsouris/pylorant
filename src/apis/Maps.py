from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import MapsModel

class Maps(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url
        
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/maps")
        response = BaseRequest.get(self, url)
        model    = MapsModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/maps/{uuid}")
        response = self.get(url)
        model    = MapsModel

        return Validator.Validate(model=model, response=response)