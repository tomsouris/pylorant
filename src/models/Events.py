from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class EventsModel(BaseModel): 
    uuid             : str        
    displayName      : str        = None
    shortDisplayName : str        = None
    startTime        : datetime   = None
    endTime          : datetime   = None
    assetPath        : str        = None
