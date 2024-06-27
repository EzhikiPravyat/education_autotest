import requests as req
import pytest
import json

access_tokens = []

#TODO работает, разнести по фкистурам, придумать как хранить токены из access_tokens для всех тестов
@pytest.mark.parametrize("username, password", [
    ("ispolnitelisp", "Test1234"),
    ("rukovoditelruk", "Test1234"),
    ("comission1", "Test1234"),
    ("predsedatelpre", "Test1234"),
    ("user_skz", "Test1234")
])
def test_auth_etp(session: req.Session, username: str, password: str):
    url = 'https://demo2-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'
    payload = json.dumps({
        "action": "Authentication",
        "method": "login",
        "data": [ username, password, None, {} ],
        "type": "rpc",
        "tid": 7,
        "token": "4LWnOKNHa9s06076FmuYxA"
    })
    response_1 = session.post(url, data=payload)

    payload = json.dumps({
        "action": "Index",
        "method": "index",
        "data": None,
        "type": "rpc",
        "tid": 13,
        "token": "4LWnOKNHa9s06076FmuYxA"
    })
    response_2 = session.post(url, data=payload)
    auth_token = response_2.json()['result']['auth_token']

    payload = json.dumps({
        "action": "User",
        "method": "getVotingLink",
        "data": [ {} ],
        "type": "rpc",
        "tid": 7,
        "token": str(auth_token)
    })
    response_3 = session.post(url, data=payload)
    link_token = response_3.json()['result']['link'].split("=")[1]

    url = f"https://api-demo-vote.etpgpb.ru/v1/auth/get-auth-data/{link_token}"
    response_3 = session.get(url)
    access_token = response_3.json()['user']['accessToken']

    print(f'access_token for {username} is {access_token}')

@pytest.mark.parametrize("token", [access_tokens])
def test_get_user_guide():
    headers = {
        "VOTE-TOKEN": access_tokens
    }
    url = "https://api-demo-vote.etpgpb.ru/v1/role"
    access_roles = ["ROLE_COMMISSION", "ROLE_COMMISSION_CHAIRMAN"]
    response = req.get(url, headers=headers)
    role = response.json()[0]
    url = "https://api-demo-vote.etpgpb.ru/v1/user-guide/ROLE_COMMISSION"
    response = req.get(url, headers=headers)
    print(role)
    if role in access_roles:
        assert response.status_code == 200
    else:
        assert response.status_code == 403