from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class PlayerCardsModel(BaseModel): 
    uuid                       : str
    displayName                : str
    isHiddenIfNotOwned         : bool
    themeUuid                  : str = None
    displayIcon                : str
    smallArt                   : str
    wideArt                    : str
    largeArt                   : str
    assetPath                  : str
