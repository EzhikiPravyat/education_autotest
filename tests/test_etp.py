import requests as req
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
    print(response.status_code)
    etpsid = response.cookies['democom_etpsid']
    print(etpsid)

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
        "token": "4LWnOKNHa9s06076FmuYxA"
}
    cookies = {
        "democom_etpsid": "l1ui9ohc4s9qg5rbm2g3orfkf5"
    }
    response = req.post(url=url, json=body, cookies=cookies)
    print(response.status_code)
    print(response.content)