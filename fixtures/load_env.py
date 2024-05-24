from dotenv import load_dotenv
from pytest import fixture
import os


load_dotenv()


@fixture()
def env():
    '''
    Получение переменной окружения
    '''
    return os.getenv