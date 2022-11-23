Звіт до роботи
Тема: Віртуальні середовища
Мета роботи: Віртуальні середовища
Виконання роботи
Основи роботи з сторонніми бібліотеками

Перевірив наявність встановленного інструменту PIP (Python Install Package) за допомогою команди
команда
pip -V
результат виконання
pip 22.3 from C:\Users\Worker\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
За допомогою команди pip --help передивися список команд які можна виконати за допомогою pip. Перевірив список встановлених на компютері бібліотек
команда
pip list
результат виконання
Package           Version
----------------- -------
asttokens         2.1.0
backcall          0.2.0
colorama          0.4.6
debugpy           1.6.3
decorator         5.1.1
entrypoints       0.4
executing         1.2.0
ipykernel         6.17.0
ipython           8.6.0
jedi              0.18.1
jupyter_client    7.4.4
jupyter_core      4.11.2
matplotlib-inline 0.1.6
nest-asyncio      1.5.6
packaging         21.3
parso             0.8.3
pickleshare       0.7.5
pip               22.3
prompt-toolkit    3.0.32
psutil            5.9.3
pure-eval         0.2.2
Pygments          2.13.0
pyparsing         3.0.9
python-dateutil   2.8.2
pywin32           305
pyzmq             24.0.1
setuptools        65.5.0
six               1.16.0
stack-data        0.6.0
tornado           6.2
traitlets         5.5.0
wcwidth           0.2.5
За допомогою команди pip install встановив бібліотеку requests
Відкривши інтерпретатор python виконав наступні команди
команди 
>>> import requests
>>> r = requests.get('https://google.com')
>>> r.status_code
>>> exit()
результат викнання r.status_code
200
Ознайомився з іншими методами бібліотеки requests. Спробував виконати деякі з них
команди
>>> import requests
>>> r = requests.post('https://httpbin.org/post', data={'key': 'value'})
>>> r.status_code
>>> exit()
результат викнання r.status_code
200
Виконав наступні команди для роботи з бібліотекою requests
команда
pip show requests
результат виконання
Name: requests
Version: 2.28.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: C:\Users\Worker\AppData\Local\Programs\Python\Python311\Lib\site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:
команда
pip install requests==2.1
результат виконання
Collecting requests==2.1
Downloading requests-2.1.0-py2.py3-none-any.whl (445 kB)
    ---------------------------------------- 445.3/445.3 kB 2.8 MB/s eta 0:00:00
Installing collected packages: requests
Attempting uninstall: requests
    Found existing installation: requests 2.28.1
    Uninstalling requests-2.28.1:
    Successfully uninstalled requests-2.28.1
Successfully installed requests-2.1.0
команда
pip show requests
результат виконання
Name: requests
Version: 2.1.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Copyright 2013 Kenneth Reitz
Location: C:\Users\Worker\AppData\Local\Programs\Python\Python311\Lib\site-packages
Requires:
Required-by:
команда
pip uninstall requests
результат виконання
Found existing installation: requests 2.1.0
Uninstalling requests-2.1.0:
Would remove:
    c:\users\worker\appdata\local\programs\python\python311\lib\site-packages\requests-2.1.0.dist-info\*
    c:\users\worker\appdata\local\programs\python\python311\lib\site-packages\requests\*
Proceed (Y/n)?
Successfully uninstalled requests-2.1.0
Робота у віртуальному середовищі

Створив віртуальне середовище VENV
команди
python -m venv ./my_env
source my_env/Scripts/activate
pip install requests
deactivate
pip show requests
результат виконання pip show requests
WARNING: Skipping reqeusts as it is not installed.
Команда pip show requests вивела помилку, тому що не знайшла встановлену бібліотеку, через то що ми інсталювали її в середені віртуального середовища, і її не видно у загальній системі;
Робота з Pipenv

За допомогою команди pip install pipenv встановив інструмент pipenv;

Список команд що можна виконати за допомогою pipenv: bash Commands: check Checks for PyUp Safety security vulnerabilities and against PEP 508 markers provided in Pipfile. clean Uninstalls all packages not specified in Pipfile.lock. graph Displays currently-installed dependency graph information. install Installs provided packages and adds them to Pipfile, or (if no packages are given), installs all packages from Pipfile. lock Generates Pipfile.lock. open View a given module in your editor. requirements Generate a requirements.txt from Pipfile.lock. run Spawns a command installed into the virtualenv. scripts Lists scripts in current environment config. shell Spawns a shell within the virtualenv. sync Installs all packages specified in Pipfile.lock. uninstall Uninstalls a provided package and removes it from Pipfile. update Runs lock, then sync. verify Verify the hash in Pipfile.lock is up-to-date.

Виконав наступні команди для створення нового середовища та інсталяції бібліотеки: bash pipenv --python 3.10 pipenv --venv pipenv run python -V pipenv install requests

У результаті виконання створилося два файли Pipfile та Pipfile.lock. У першому список бібліотек та залежностей, у другому json обєкт з хеш сумами;

Створив пайтон файл з наступним змістом: ```python import requests

 response = requests.get('https://httpbin.org/')
 for line in response.iter_lines():
     print(line)
 ```
При виконанні програми з Visual Studio чи з командної стрічки видає помилку:

Traceback (most recent call last):
File "C:\python_labs\lab 6\lab6.py", line 1, in 
    import requests
ModuleNotFoundError: No module named 'requests'
Після входу у віртуальне середовища за допомогою команди pipenv shell та виконання прогрми там, отримав html код вказаної веб-сторінки;

...
b''
b'    '
b'    httpbin.org'
b'    
b'        rel="stylesheet">'
b'    '
b'    '
b'    '
b''
...
Передивився різні бібліотеки на Pypi та інсталював camelcase. Написам програму для демонстрації роботи бібліотеки

код програми

import camelcase
from camelcase import CamelCase

c = CamelCase()
s  = 'this is a sentence that needs CamelCasing!'
print(c.hump(s))
результат виконання

This is a Sentence That Needs CamelCasing!
Переглянув список доступних інтерпретаторів за допомогою команди Python: Select interpreter



Робота зі змінними середовища

Створив файл .env та виконав наступний код: python import os os.environ['HELLO']

При виконанні коду без активації віртуального середовища отривам помилку: ```text Exception has occurred: KeyError 'HELLO'

     During handling of the above exception, another exception occurred:

     File "C:\python_labs\lab 6\lab6-3.py", line 2, in 
         os.environ['HELLO']
 ```
![image](https://raw.githubusercontent.com/ArtemDidukh/Registration-and-submission-of-works/main/Lab/Lab6/img1.png)

Висновок:
В ході роботи я ознаймився з основами роботи із сторонніми бібліотеками, їх інсталяція та управління. Навчився встановлювати та налаштовлувати віртуальні середовища, працювати з ними;
Так, мету роботи досягнуто.
Всі, згідно вищезазначених завдань
У даній роботі питання відсутні)
Так, вдалось
Ні, не виникало.
Так, подобається.
Зменшити кількість питань у висновку)
