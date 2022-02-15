from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import CompetitiveTiersModel

class CompetitiveTier(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url
        
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/competitivetiers")
        response = BaseRequest.get(self, url)
        model    = CompetitiveTiersModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/competitivetiers/{uuid}")
        response = self.get(url)
        model    = CompetitiveTiersModel

        return Validator.Validate(model=model, response=response)