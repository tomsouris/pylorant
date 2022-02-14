from marshmallow import Schema, fields

class MediaList(Schema):
    id    = fields.Int()
    wwise = fields.Str()
    wave  = fields.Str()

class VoiceLine(Schema):
    minDuration = fields.Int()
    maxDuration = fields.Int()
    mediaList   = fields.Nested(MediaList, many=True)

class Role(Schema):
    uuid        = fields.Str()
    displayName = fields.Str()
    description = fields.Str()
    displayIcon = fields.Str()
    assetPath   = fields.Str()

class Abilities(Schema):
    slot        = fields.Str()
    displayName = fields.Str()
    description = fields.Str()
    displayIcon = fields.Str()

class AgentModel(Schema):
    uuid                      = fields.Str()
    displayName               = fields.Str()
    description               = fields.Str()
    developerName             = fields.Str()
    characterTags             = fields.Raw()
    displayIcon               = fields.Str()
    displayIconSmall          = fields.Str()
    bustPortrait              = fields.Str()
    fullPortrait              = fields.Str()
    killfeedPortrait          = fields.Str()
    assetPath                 = fields.Str()
    background                = fields.Str()
    isFullPortraitRightFacing = fields.Bool()
    isPlayableCharacter       = fields.Bool()
    isAvailableForTest        = fields.Bool()
    isBaseContent             = fields.Bool()
    role                      = fields.Nested(Role())
    abilities                 = fields.Nested(Abilities, many=True)
    voiceLine                 = fields.Nested(VoiceLine())

