from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import VersionModel

class Version(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url
        
    def current(self):
        url      = UrlBuilder.url(self.base_url, "/version")
        response = BaseRequest.get(self, url)
        model    = VersionModel

        return Validator.Validate(model=model, response=response)