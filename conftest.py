import glob
from os.path import join
from pathlib import Path
from platform import system

'''
Подключение фикстур к проекту
'''
def get_fixtures():
    fixtures = join(Path(__file__).parent, 'fixtures')
    file_path = []
    for file in glob.glob(f'{fixtures}/*'):
        if system().lower() in ['linux', 'darwin']:
            file = file.split('/') 
        else:
            file = file.split('\\')
        file = file[-1].split('.')[0]
        if file not in ['__init__', '__pycache__']:
            file_path.append(f'fixtures.{file}')
        return file_path
    


pytest_plugins = get_fixtures() #Подключение всех фиксктур в проекту