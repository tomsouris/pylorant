from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class SeasonsModel(BaseModel): 
    uuid                : str
    displayName         : str
    type                : str = None
    startTime           : datetime
    endTime             : datetime
    parentUuid          : str = None
    background          : str = None
    assetPath           : str = None

class BorderModel(BaseModel):
    uuid                  : str
    level                 : int
    winsRequired          : int
    displayIcon           : str
    smallIcon             : str = None
    assetPath             : str

class CompetitiveSeasonsModel(BaseModel): 
    uuid                  : str = None
    startTime             : datetime
    endTime               : datetime
    seasonUuid            : str = None
    competitiveTiersUuid  : str = None
    borders               : List[BorderModel] = None
    assetPath             : str = None