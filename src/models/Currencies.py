from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class CurrenciesModel(BaseModel): 
    uuid                      : str = None
    displayName               : str = None
    displayNameSingular       : str = None
    displayIcon               : str = None
    largeIcon                 : str = None
    assetPath                 : str = None
