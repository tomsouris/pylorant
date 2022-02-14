from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import BuddiesModel, BuddieLevelsModel

class Buddies(BaseRequest):
    def __init__(self):
        super().__init__(5.00)
        self.base_url = BaseRequestConfig.base_url
        # self.timeout = 5.01
        
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/buddies")
        response = BaseRequest.get(self, url)
        model    = BuddiesModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/buddies/{uuid}")
        response = self.get(url)
        model    = BuddiesModel

        return Validator.Validate(model=model, response=response)
    
    def levels(self):
        url      = UrlBuilder.url(self.base_url, f"/buddies/levels")
        response = self.get(self, url)
        model    = BuddieLevelsModel

        return Validator.Validate(model=model, response=response)

    def levels_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/buddies/levels/{uuid}")
        response = BaseRequest.get(self, url)
        model    = BuddieLevelsModel

        return Validator.Validate(model=model, response=response)