import requests as req
from pytest import fixture, mark
import json

auth_token = None
link_token = None

def test_auth_etp(session: req.Session):
    url = 'https://demo2-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'
    payload = json.dumps({
        "action": "Authentication",
        "method": "login",
        "data": [ "comission1", "Test1234", "null", {} ],
        "type": "rpc",
        "tid": 7,
        "token": "4LWnOKNHa9s06076FmuYxA"
    })
    response = session.post(url, data=payload)

def test_token(session: req.Session):
    global auth_token
    url = 'https://demo2-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'
    payload = json.dumps({
        "action": "Index",
        "method": "index",
        "data": None,
        "type": "rpc",
        "tid": 13,
        "token": "0bCWL8aaWIc5gDsY4K5KIg"
    })
    response = session.post(url, data=payload)
    auth_token = response.json()['result']['auth_token']

def test_voting_link(session: req.Session):
    global link_token
    url = 'https://demo2-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'
    payload = json.dumps({
        "action": "User",
        "method": "getVotingLink",
        "data": [ {} ],
        "type": "rpc",
        "tid": 7,
        "token": str(auth_token)
    })
    response = session.post(url, data=payload)
    link_token = response.json()['result']['link'].split("=")[1]

def test_auth_ec(session: req.Session):
    url = f"https://api-demo-vote.etpgpb.ru/v1/auth/get-auth-data/{link_token}"
    response = session.get(url)
    print(response.json()['user']['accessToken'])

def test_get_user_guide():
    headers = {
        "VOTE-TOKEN": "c8052599c9a6f6d3e6197188df1faac09566b410"
    }
    url = "https://api-demo-vote.etpgpb.ru/v1/role"
    access_roles = ["ROLE_COMMISSION", "ROLE_COMMISSION_CHAIRMAN"]
    response = req.get(url, headers=headers)
    role = response.json()[0]
    url = "https://api-demo-vote.etpgpb.ru/v1/user-guide/ROLE_COMMISSION"
    response = req.get(url, headers=headers)
    if role in access_roles:
        assert response.status_code == 200
    else:
        assert response.status_code == 403