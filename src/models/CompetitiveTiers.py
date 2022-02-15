from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class TiersModel(BaseModel): 
    tier                 : int = None
    tierName             : str = None
    division             : str = None
    divisionName         : str = None
    color                : str = None
    backgroundColor      : str = None
    smallIcon            : str = None
    largeIcon            : str = None
    rankTriangleDownIcon : str = None
    rankTriangleUpIcon   : str = None

class CompetitiveTiersModel(BaseModel):
    uuid                   : str
    assetObjectName        : str
    tiers                  : List[TiersModel]
    assetPath              : str