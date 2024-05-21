import requests as req
import pytest
import re

def test_smoke_fields(get, put):
    #url = 'https://demo-passport.etpgpb.ru/api/v2/dictionaries/oksm'
    #response = get(url=url)
    url = 'https://demo-passport.etpgpb.ru/api/v2/user/profile'

    body = {
        "firstName": "Shelley",
        "lastName": "Sloan",
        "middleName": "Eeooniekkkeee",
        "timezone": "(UTC+10:00) Asia/Vladivostok",
        "timezoneTitle": "(UTC+10:00) Владивосток",
        "phone": "74706805653",
        "phoneExt": "2",
        "job": "Генеральный директор"
}
    response = put(url=url, json=body)
    response_json = response.json()

    print(response.status_code)
    print(response.content)

    assert response.headers['content-type'] == 'application/json', f'content-type is not application/json'
    assert 'data' in response_json
    assert 'errors' in response_json
    assert 'requestId' in response_json

    assert isinstance(response_json['requestId'], str), f'requestId is not string'
    assert bool(re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', 
                            response_json['requestId'])) == True, f'requestId is not UUID'
    
    status_codes = [400, 401, 403, 500]

    if (response.status_code == 200):
        assert response_json['errors'] is None, f'errors is not None'

    elif response.status_code in status_codes:
        assert response_json['errors'] is not None, f'errors is None'
        errors = response_json['errors'][0]
        print(errors)
        assert isinstance(errors, dict)
        assert 'title' in errors
        assert 'detail' in errors
        assert 'reasonCode' in errors
        assert isinstance(errors['title'], str)
        assert isinstance(errors['detail'], str)
        assert isinstance(errors['reasonCode'], str)
    else:
        print('Something wrong')
        pytest.fail

# def test_auth_etp():
#     url = 'https://chernobrivets-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'

#     body = {
#         "action": "Authentication",
#         "method": "login",
#         "data": [
#             "isp",
#             "Privet111",
#             "null",
#             {}
#         ],
#         "type": "rpc",
#         "tid": 7,
#         "token": "4LWnOKNHa9s06076FmuYxA"
# }
#     response = req.post(url=url, json=body)
#     print(response.status_code)
#     etpsid = response.cookies['democom_etpsid']
#     print(etpsid)

# def test_get_token():
#     url = 'https://chernobrivets-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'

#     body = {
#         "action": "User",
#         "method": "getVotingLink",
#         "data": [
#             {}
#         ],
#         "type": "rpc",
#         "tid": 7,
#         "token": "4LWnOKNHa9s06076FmuYxA"
# }
#     cookies = {
#         "democom_etpsid": "k4goeom68m1mlv88qev438667h"
#     }
#     response = req.post(url=url, json=body, cookies=cookies)
#     print(response.status_code)
#     print(response.content)