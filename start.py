import os
import threading
cmd = 'py'


def start_server():
    try:
        os.system(f'{cmd} app.py')
    except Exception as ex:
        print(f'ERROR : {ex}')


def start_discord_bot():
    try:
        os.system(f'{cmd} botty.py')
    except Exception as ex:
        print(f'ERROR : {ex}')


thread1 = threading.Thread(target=start_server)
thread2 = threading.Thread(target=start_discord_bot)

thread1.start()
thread2.start()
