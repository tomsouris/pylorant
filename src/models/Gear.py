from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class GridPositionModel(BaseModel): 
    row                         : int
    column                      : int

class shopDataModel(BaseModel): 
    cost                    : int
    category                : str
    categoryText            : str
    gridPosition            : GridPositionModel = None
    canBeTrashed            : bool
    image                   : str = None
    newImage                : str
    newImage2               : str = None
    assetPath               : str

class GearModel(BaseModel):
    uuid                      : str
    displayName               : str
    description               : str
    displayIcon               : str
    assetPath                 : str
    shopData                  : shopDataModel
    background                : str  = None
    isFullPortraitRightFacing : bool = None

