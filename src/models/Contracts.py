from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class RewardModel(BaseModel): 
    type                  : str
    uuid                  : str
    amount                : int
    isHighlighted         : bool

class LevelsModel(BaseModel): 
    reward                : RewardModel
    xp                    : int
    vpCost                : int
    isPurchasableWithVP   : bool

class ChaptersModel(BaseModel) : 
    isEpilogue               : str                 = None
    levels                   : List[LevelsModel]   = None
    premiumRewardScheduleUuid: str                 = None
    premiumVPCost            : str                 = None

class ContentModel(BaseModel):
    relationType             : str                 = None
    relationUuid             : str                 = None
    chapters                 : List[ChaptersModel] = None

class ContractsModel(BaseModel): 
    uuid                     : str
    displayName              : str  = None
    displayIcon              : str  = None
    shipIt                   : bool = None
    freeRewardScheduleUuid   : str  = None
    content                  : ContentModel
    assetPath                : str