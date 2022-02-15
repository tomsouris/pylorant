from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class VersionModel(BaseModel): 
    manifestId             : str
    branch                 : str
    version                : str = None
    buildVersion           : str = None
    riotClientVersion      : str
    buildDate              : datetime