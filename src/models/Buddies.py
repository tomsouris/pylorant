from marshmallow import Schema, fields

class BuddieLevelsModel(Schema):
    uuid        = fields.Str()
    charmLevel  = fields.Int()
    displayName = fields.Str()
    displayIcon = fields.Str()
    assetPath   = fields.Str()

class BuddiesModel(Schema):
    uuid               = fields.Str()
    displayName        = fields.Str()
    isHiddenIfNotOwned = fields.Bool()
    themeUuid          = fields.Str(allow_none=True)
    displayIcon        = fields.Str()
    assetPath          = fields.Str()
    levels             = fields.Nested(BuddieLevelsModel, many=True)

