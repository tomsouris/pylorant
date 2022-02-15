from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class ContentTiersModel(BaseModel): 
    uuid                 : str 
    devName              : str = None
    highlightColor       : str = None
    displayIcon          : str = None
    assetPath            : str = None
