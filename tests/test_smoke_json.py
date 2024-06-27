from jsonschema import validate
from pytest import mark
from fixtures.read_json import read_config_json
import allure

@allure.epic("API")
@allure.feature('Smoke test')
@allure.description('Проверяет возможность обновления данных в ЛК пользователя')
@allure.title('Обновление данных в карточке пользователя')
@mark.usefixtures('session')
def test_put_user_profile(put, valid_scheme_put_user_profile):
    config_data = read_config_json("/api/v2/user/profile")
    with allure.step('PUT запрос к /api/v2/user/profile'):
        response = put(url=config_data['url'], json=config_data['body'])

    assert response.status_code in (200, 401)
    print(response.status_code)
    if response.status_code == 200:
        validate(instance=response.json(), schema=valid_scheme_put_user_profile[0])
    else:
        validate(instance=response.json(), schema=valid_scheme_put_user_profile[1])