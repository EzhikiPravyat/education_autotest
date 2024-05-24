import requests as req
from pytest import fixture, mark
import json

def test_run(session: req.Session):
    test_auth_etp(session)
    auth_token = test_token(session)
    link_token =  test_voting_link(auth_token, session)
    test_auth_ec(link_token, session)

def test_auth_etp(session: req.Session):
    url = 'https://demo2-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'
    payload = json.dumps({
        "action": "Authentication",
        "method": "login",
        "data": [
            "ispolnitelisp",
            "Test1234",
            "null",
            {}
        ],
        "type": "rpc",
        "tid": 7,
        "token": "4LWnOKNHa9s06076FmuYxA"
    })
    response = session.post(url, data=payload)

def test_token(session: req.Session):
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
    return response.json()['result']['auth_token']

def test_voting_link(auth_token: str, session: req.Session):
    url = 'https://demo2-gaz.etpgpb.ru/index.php?rpctype=direct&module=default&client=etp'
    payload = json.dumps({
        "action": "User",
        "method": "getVotingLink",
        "data": [
            {}
        ],
        "type": "rpc",
        "tid": 7,
        "token": str(auth_token)
    })
    response = session.post(url, data=payload)
    link_token = response.json()['result']['link'].split("=")[1]
    return link_token

def test_auth_ec(link_token: str, session: req.Session):
    url = f"https://api-demo-vote.etpgpb.ru/v1/auth/get-auth-data/{link_token}"
    response = session.get(url)
    print(response.json()['user']['accessToken'])
    print(response.text)