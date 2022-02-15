from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class BundlesModel(BaseModel): 
    uuid                   : str
    displayName            : str
    displayNameSubText     : str
    description            : str
    extraDescription       : str
    promoDescription       : str
    useAdditionalContext   : bool
    displayIcon            : str
    displayIcon2           : str
    verticalPromoImage     : str
    assetPath              : str