from pytest import fixture


@fixture
def post_etp(session):
    """
    Фикстура для POST запроса с использованием сессии.
    """
    def _post_etp(url, data):
        response = session.post(url=url, data=data)
        return response
    return _post_etp