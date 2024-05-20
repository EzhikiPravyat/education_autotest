import requests as req
import pytest
import json

def test_get_oksm(get):
    url = 'https://demo-passport.etpgpb.ru/api/v2/dictionaries/oksm'

    response = get(url=url)
    response_json = response.json()
    print(response.status_code)
    print(response.content)

    try:
        assert response.status_code == 200, 'Status code is not 200'
        assert response.headers['content-type'] == 'application/json', f'content-type is not application/json'
        assert response_json['errors'] == None, f'Errors in not None'
        assert type(response_json['requestId']) == str, f'requestId is not string'
    except:
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