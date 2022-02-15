from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class MediaList(BaseModel):
    id    : int
    wwise : str
    wave  : str

class VoiceLine(BaseModel):
    minDuration : int
    maxDuration : int
    mediaList   : List[MediaList]

class Role(BaseModel):
    uuid        : str
    displayName : str
    description : str
    displayIcon : str
    assetPath   : str

class Abilities(BaseModel):
    slot        : str
    displayName : str
    description : str
    displayIcon : str = None

class AgentModel(BaseModel):
    uuid                      : str
    displayName               : str
    description               : str
    developerName             : str
    # characterTags             : str = None
    displayIcon               : str
    displayIconSmall          : str
    bustPortrait              : str = None
    fullPortrait              : str = None
    killfeedPortrait          : str
    assetPath                 : str
    background                : str = None
    isFullPortraitRightFacing : bool
    isPlayableCharacter       : bool
    isAvailableForTest        : bool
    isBaseContent             : bool
    role                      : Role = None
    abilities                 : List[Abilities]
    voiceLine                 : VoiceLine

