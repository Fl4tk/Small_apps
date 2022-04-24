import pyautogui as pag
import time

dirname = input('新規ディレクトリ名入力')
projectname = input('プロジェクト名入力')

pag.press('win')
time.sleep(1)
pag.typewrite('Ubuntu')
pag.press('enter')

time.sleep(2)

pag.typewrite('code .')
pag.press('enter')
time.sleep(7)
pag.hotkey('ctrl','j')
time.sleep(3)
pag.typewrite('cd django')
pag.press('enter')
time.sleep(2)
pag.typewrite(f'mkdir {dirname}')
pag.press('enter')
time.sleep(2)
pag.typewrite(f'cd {dirname}')
pag.press('enter')
time.sleep(2)
pag.typewrite('python3 -m venv venv')
pag.press('enter')
time.sleep(2)
pag.typewrite('source venv/bin/activate')
pag.press('enter')
time.sleep(2)
pag.typewrite('pip install django==3.2')
pag.press('enter')
time.sleep(7)
pag.typewrite(f'django-admin startproject {projectname}')
pag.press('enter')
time.sleep(2)
pag.typewrite(f'cd {projectname}')
pag.press('enter')