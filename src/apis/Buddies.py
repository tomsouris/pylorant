from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, JsonValidate
from ..models import BuddiesModel, BuddieLevelsModel

class Buddies(BaseRequest):
    def __init__(self):
        self.base_url = BaseRequestConfig.base_url
        super().__init__()
        
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/buddies")
        response = BaseRequest.get(self, url)
        model    = BuddiesModel()

        return JsonValidate.Validate(model=model, response=response, isArray=True)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/buddies/{uuid}")
        response = BaseRequest.get(self, url)
        model    = BuddiesModel()

        return JsonValidate.Validate(model=model, response=response, isArray=False)
    
    def levels(self):
        url      = UrlBuilder.url(self.base_url, f"/buddies/levels")
        response = BaseRequest.get(self, url)
        model    = BuddieLevelsModel()

        return JsonValidate.Validate(model=model, response=response, isArray=True)

    def levels_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/buddies/levels/{uuid}")
        response = BaseRequest.get(self, url)
        model    = BuddieLevelsModel()

        return JsonValidate.Validate(model=model, response=response, isArray=False)