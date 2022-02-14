from marshmallow import Schema, fields
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class BuddieLevelsModel(BaseModel):
    uuid        : str
    charmLevel  : int
    displayName : str
    displayIcon : str
    assetPath   : str

class BuddiesModel(BaseModel):
    uuid               : str
    displayName        : str
    isHiddenIfNotOwned : bool
    themeUuid          : str = None
    displayIcon        : str
    assetPath          : str
    # levels             : Nested(BuddieLevelsModel, many=True)
    levels             : List[BuddieLevelsModel]

