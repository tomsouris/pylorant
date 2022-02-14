from marshmallow.exceptions import ValidationError

class JsonValidate:
    def Validate(model, response, isArray=False):
        try:
            return model.load(response["data"], many=isArray )
        except ValidationError as err :
            return err