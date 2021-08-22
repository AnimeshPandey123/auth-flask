from exceptions.validationexception import ValidationException
from jsonschema import Draft7Validator,FormatChecker
from jsonschema.validators import validate

login_schema = {
   'type': 'object',
   'properties': {
       'email': {
            "description": "Email of the user",
           'type': 'string',
           "format": "email"
       },
        'password': {
            'type': 'string', 'minimum': 6  
       }
   },
   'required': ['email', 'password']
}

class LoginValidator:

    def validate(request):
        list = []
        # try:
        #     validate(request, schema=login_schema)
        # except Exception as e:
        #     list.append(str(e.args))
        #     list.append(str(e))
        v = Draft7Validator(schema=login_schema,
            format_checker=FormatChecker())
        
        for error in sorted(v.iter_errors(request), key=str):
            list.append(error.message)
        if list:
            raise ValidationException(list)
   