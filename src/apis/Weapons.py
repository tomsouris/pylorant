from ..base import BaseRequest
from ..config import BaseRequestConfig
from ..mixins import UrlBuilder, Validator
from ..models import WeaponsModel, WeaponSkinsModel, ChromasModel, LevelsModel

class Weapons(BaseRequest):
    def __init__(self):
        super().__init__()
        self.base_url = BaseRequestConfig.base_url
        
        """
        Weapons
        """
    def all(self):
        url      = UrlBuilder.url(self.base_url, "/weapons")
        response = BaseRequest.get(self, url)
        model    = WeaponsModel

        return Validator.Validate(model=model, response=response)
    
    def by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/weapons/{uuid}")
        response = self.get(url)
        model    = WeaponsModel

        return Validator.Validate(model=model, response=response)

        """
        Weapon Skins
        """
        
    def skins_all(self):
        url      = UrlBuilder.url(self.base_url, "/weapons/skins")
        response = BaseRequest.get(self, url)
        model    = WeaponSkinsModel

        return Validator.Validate(model=model, response=response)

    def skins_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/weapons/{uuid}")
        response = BaseRequest.get(self, url)
        model    = WeaponSkinsModel

        """
        Weapon Skins Chromas
        """

    def skins_chroma_all(self):
        url      = UrlBuilder.url(self.base_url, "/weapons/skinchromas")
        response = BaseRequest.get(self, url)
        model    = ChromasModel

        return Validator.Validate(model=model, response=response)

    def skins_chroma_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/weapons/skinchromas/{uuid}")
        response = BaseRequest.get(self, url)
        model    = ChromasModel

        return Validator.Validate(model=model, response=response)

        """
        Weapon Skins Levels
        """

    def skins_levels_all(self):
        url      = UrlBuilder.url(self.base_url, "/weapons/skinlevels")
        response = BaseRequest.get(self, url)
        model    = LevelsModel

        return Validator.Validate(model=model, response=response)

    def skins_levels_by_uuid(self, uuid):
        url      = UrlBuilder.url(self.base_url, f"/weapons/skinlevels/{uuid}")
        response = BaseRequest.get(self, url)
        model    = LevelsModel

        return Validator.Validate(model=model, response=response)