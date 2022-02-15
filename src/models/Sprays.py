from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class SprayLevelModel(BaseModel): 
    uuid                 : str
    sprayLevel           : int
    displayName          : str = None
    displayIcon          : str
    assetPath            : str = None

class SprayModel(BaseModel): 
    uuid                              : str
    displayName                       : str = None
    category                          : str = None
    themeUuid                         : str = None
    displayIcon                       : str = None
    fullIcon                          : str = None
    fullTransparentIcon               : str = None
    assetPath                         : str = None
    levels                            : List[SprayLevelModel] = None