import os

'''
Подключение фикстур к проекту
'''
def get_fixtures():
    fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
    file_path = []
    for file in os.listdir(fixtures_dir):
        if file != '__init__.py' and file != '__pycache__':
            file_path.append(f'fixtures.{os.path.splitext(file)[0]}')
    return file_path

pytest_plugins = get_fixtures() #Подключение всех фиксктур в проекту
print(pytest_plugins)