from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class BundlesModel(BaseModel): 
    uuid                   : str
    displayName            : str
    displayNameSubText     : str = None
    description            : str
    extraDescription       : str = None
    promoDescription       : str = None
    useAdditionalContext   : bool
    displayIcon            : str
    displayIcon2           : str
    verticalPromoImage     : str = None
    assetPath              : str