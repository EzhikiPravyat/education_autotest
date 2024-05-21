from jsonschema import validate
from pytest import mark


@mark.usefixtures('session') ##Перед запуском теста выполяется предусловие, в данном случае session
def test_put_user_profile(put, valid_scheme_put_user_profile):
    url = 'https://demo-passport.etpgpb.ru/api/v2/user/profile'

    body = {
        "firstName": "Shelley",
        "lastName": "Sloan",
        "middleName": "Eeooniekkkeee",
        "timezone": "(UTC+10:00) Asia/Vladivostok",
        "timezoneTitle": "(UTC+10:00) Владивосток",
        "phone": "74706805653",
        "phoneExt": "2",
        "job": "Генеральный директор"
    }

    response = put(url=url, json=body)
    print(response.status_code)
    if (response.status_code == 200):
        validate(instance=response.json(), schema=valid_scheme_put_user_profile[0])
    else:
        validate(instance=response.json(), schema=valid_scheme_put_user_profile[1])
    