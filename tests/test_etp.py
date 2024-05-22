import requests as req
import pytest
from pytest import fixture
from pytest import mark

@mark.usefixtures('session')
def test_auth_etp():
    url = 'https://chernobrivets-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'

    body = {
        "action": "Authentication",
        "method": "login",
        "data": [
            "isp",
            "Privet111",
            "null",
            {}
        ],
        "type": "rpc",
        "tid": 7,
        "token": "4LWnOKNHa9s06076FmuYxA"
}
    response = req.post(url=url, json=body)
    etpsid = response.cookies['democom_etpsid']

@mark.usefixtures('session')
def test_get_token():
    url = 'https://chernobrivets-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'

    body = {
        "action": "User",
        "method": "getVotingLink",
        "data": [
            {}
        ],
        "type": "rpc",
        "tid": 7,
        "token": "/pEqG6V34Mb9LKLbPYAUTQ"
}
    cookies = {
        "democom_etpsid": "gg5kdd32ec1u1fcbk2tc47fmsi"
    }
    response = req.post(url=url, json=body, cookies=cookies)
    print(response.cookies)
    print(response.status_code)
    # if (response.json()['success'] == 'true'):
    #     etpcode = response.json()['result']['link'].split("=")[1]
    # else:
    #     pytest.fail