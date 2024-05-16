import sys, pytest, os, json
# from dotenv import load_dotenv
from os.path import join
from pathlib import Path
from pytest import fixture
import requests as req

@fixture()
def get_one():
    '''
    Тестовая фикстура
    '''
    print("i am here")
    return "1"