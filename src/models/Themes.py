from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class ThemesModel(BaseModel): 
    uuid                  : str
    displayName           : str
    displayIcon           : str = None
    storeFeaturedImage    : str = None
    assetPath             : str
