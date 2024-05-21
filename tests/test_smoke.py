import requests as req
import pytest
import re

def test_put_user_profile(put):
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
        assert isinstance(response_json['errors'][0], dict)
        errors_keys = ['title', 'detail', 'reasonCode']
        for key in response_json['errors'][0]:
            assert key in errors_keys
            assert isinstance(key, str)
    else:
        print('Something wrong')
        pytest.fail

def test_get_dictionaries_oksm(get):
    url = 'https://demo-passport.etpgpb.ru/api/v2/dictionaries/oksm'
    response = get(url=url)
    response_json = response.json()

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
        assert len(response_json['data']) == 246, f'OKSM is not full = 246'
        assert isinstance(response_json['data'][0], dict)
        data_keys = ['id', 'shortName', 'globalId', 'fullName', 'code', 'alpha2', 'alpha3', 'isoNr', 
                     'currencyAlpha3', 'currencyTitle', 'phoneCode', 'internetDomain', 'title', 'fullTitle', 
                     'location', 'locationPrecise', 'display', 'oosName', 'sng', 'nsiTitle', 'priority', 'active', 'independent']

        for key in response_json['data'][0]:
            assert key in data_keys
            assert isinstance(key, str)

    elif response.status_code in status_codes:
        assert response_json['errors'] is not None, f'errors is None'
        assert isinstance(response_json['errors'][0], dict)
        errors_keys = ['title', 'detail', 'reasonCode']
        for key in response_json['errors'][0]:
            assert key in errors_keys
            assert isinstance(key, str)
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