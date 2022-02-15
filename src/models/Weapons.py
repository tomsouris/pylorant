from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

class LevelsModel(BaseModel): 
    uuid            : str
    displayName     : str = None
    levelItem       : str = None
    displayIcon     : str = None
    streamedVideo   : str = None
    assetPath       : str

class ChromasModel(BaseModel): 
    uuid                   : str
    displayName            : str = None
    displayIcon            : str = None
    fullRender             : str = None
    swatch                 : str = None
    streamedVideo          : str = None
    assetPath              : str

class SkinsModel(BaseModel): 
    uuid                 : str
    displayName          : str = None
    themeUuid            : str = None
    contentTierUuid      : str
    displayIcon          : str = None
    wallpaper            : str = None
    assetPath            : str
    chromas              : ChromasModel
    levels               : LevelsModel = None

class GridPositionModel(BaseModel): 
    row                         : int
    column                      : int
    
class ShopDataModel(BaseModel): 
    cost                    : int
    category                : str
    categoryText            : str
    gridPosition            : GridPositionModel
    canBeTrashed            : bool
    image                   : str
    newImage                : str
    newImage2               : str
    assetPath               : str

class DamageRangesModel(BaseModel): 
    rangeStartMeters            : str
    rangeEndMeters              : str
    headDamage                  : str
    bodyDamage                  : str
    legDamage                   : str

class AirBurstStatsModel(BaseModel): 
    shotgunPelletCount           : int
    burstDistance                : str

class AltShotgunStatsModel(BaseModel): 
    shotgunPelletCount             : int
    burstRate                      : int

class AdsStatsModel(BaseModel): 
    zoomMultiplier          : str
    fireRate                : str
    runSpeedMultiplier      : str
    burstCount              : int
    firstBulletAccuracy     : str

class WeaponStatsModel(BaseModel): 
    fireRate                   : str
    magazineSize               : int
    runSpeedMultiplier         : str = None
    equipTimeSeconds           : str = None
    reloadTimeSeconds          : str
    firstBulletAccuracy        : str
    shotgunPelletCount         : int
    wallPenetration            : str
    feature                    : str = None
    fireMode                   : str = None
    altFireType                : str = None
    adsStats                   : AdsStatsModel = None
    altShotgunStats            : AltShotgunStatsModel = None
    airBurstStats              : AirBurstStatsModel = None
    damageRanges               : List[DamageRangesModel] = None
    shopData                   : ShopDataModel = None
    skins                      : SkinsModel = None

class WeaponSkinsModel(BaseModel): 
    uuid                       : str
    displayName                : str = None
    themeUuid                  : str = None
    contentTierUuid            : str = None
    displayIcon                : str = None
    wallpaper                  : str = None
    assetPath                  : str
    chromas                    : List[ChromasModel] = None
    levels                     : List[LevelsModel]  = None

class WeaponsModel(BaseModel): 
    uuid                  : str
    displayName           : str = None
    category              : str = None
    defaultSkinUuid       : str = None
    displayIcon           : str = None
    killStreamIcon        : str = None
    assetPath             : str
    weaponStats           : WeaponStatsModel = None