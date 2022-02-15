from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class CeremoniesModel(BaseModel): 
    uuid                 : str
    displayName          : str
    assetPath            : str



