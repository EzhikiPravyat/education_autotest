from pytest import fixture

@fixture()
def valid_scheme_put_user_profile():
    '''
    Схема для /api/v2/user/profile для 
    1) status_code = 200
    2) status_code = 400, 401, 403, 500
    '''
    return [{
        "type": "object",
        "properties": {
            "errors": {"type": ["null", "string"]},
            "data": {"type": ["null", "array"]},
            "requestId": {"type": "string", "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"}
        },
        "required": ["errors", "data", "requestId"]
    }, 
    {
        "type": "object",
        "properties": {
            "data": {"type": "null"},
            "errors": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "detail": {"type": "string"},
                        "reasonCode": {"type": "string", "default": ""}
                    },
                    "required": ["title", "detail"]
                }
            },
            "requestId": {"type": "string"}
        },
        "required": ["data", "errors", "requestId"]
    }]