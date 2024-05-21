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
def post(headers):
    def req_post(**kwargs):
        kwargs['headers'] = headers
        return req.post(**kwargs)
    return req_post

@fixture()
def put(headers):
    def req_put(**kwargs):
        kwargs['headers'] = headers
        return req.put(**kwargs)
    return req_put

def delete(headers):
    def req_delete(**kwargs):
        kwargs['headers'] = headers
        return req.delete(**kwargs)
    return req_delete

@fixture()
def headers(env):
    return {
        "Authorization": env('token_bearer')
    }