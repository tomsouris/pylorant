from pydantic import ValidationError

class Validator:
    def Validate(model, response):
        try:
            return model(**response["data"]) 
        except ValidationError as err :
            print(err)
            return err