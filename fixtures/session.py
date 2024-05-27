from pytest import fixture
import requests as req


@fixture()
def session():
    '''
    Подключение и отключение сессии
    '''
    print('\n', "-" * 70, "Session start", "-" * 70)
    s = req.Session()
    yield s
    s.close()
    print('\n', "-" * 70, "Session close", "-" * 70)