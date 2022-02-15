from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class LocationModel(BaseModel): 
    x                       : str
    y                       : str

class CalloutsModel(BaseModel): 
    regionName              : str
    superRegionName         : str
    location                : LocationModel

class MapsModel(BaseModel): 
    uuid                 : str
    displayName          : str
    coordinates          : str
    displayIcon          : str = None
    listViewIcon         : str = None
    splash               : str
    assetPath            : str
    mapUrl               : str
    xMultiplier          : str
    yMultiplier          : str
    xScalarToAdd         : str
    yScalarToAdd         : str
    callouts             : List[CalloutsModel] = None

