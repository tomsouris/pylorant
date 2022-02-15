from pydantic import ValidationError

class Validator:
    def Validate(model, response):
        if not isinstance(response["data"], list):
            try:
                return model(**response["data"]) 
            except ValidationError as err :
                print(err)
                return err
        else: 
            final = []
            for element in response["data"]:
                m = model(**element) 
                final.append(m)
            return final