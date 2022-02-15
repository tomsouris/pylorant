from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel


class GameRuleBoolOverridesModel(BaseModel): 
    ruleName     : str
    state        : str

class GameFeatureOverridesModel(BaseModel): 
    featureName  : str
    state        : bool

class GameModesModel(BaseModel): 
    uuid                     : str
    displayName              : str
    duration                 : str = None
    allowsMatchTimeouts      : str = None
    isTeamVoiceAllowed       : str = None
    isMinimapHidden          : str = None
    orbCount                 : str = None
    teamRoles                : List[str] = None
    gameFeatureOverrides     : List[GameFeatureOverridesModel]  = None
    gameRuleBoolOverrides    : List[GameRuleBoolOverridesModel] = None
    displayIcon              : str = None
    assetPath                : str = None
