import os
from dotenv import load_dotenv
from pytest import fixture
import requests as req

load_dotenv() #вызов функции для подключения env

@fixture()
def env():
    return os.getenv

@fixture()
def get(headers):
    def req_get(**kwargs):
        kwargs['headers'] = headers
        return req.get(**kwargs)
    return req_get

@fixture()
def headers(env):
    return {
        "Authorization": env('token_bearer')
    }