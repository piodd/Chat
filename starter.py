from user_interface.Window import Window
from user_interface.setting import Setting
from user_interface.login_window import LoginWindow
from client.client import Client
from client.client import ClientSetting
from client.connector import Connector
import threading
import time

setting = Setting("chat room", 800, 800)

login_window = LoginWindow(setting)

client_setting = ClientSetting(setting.user_name)

client = Client(client_setting)
window = Window(setting)

connector = Connector(client, window)
client.import_connector(connector)
window.import_connector(connector)

client_thread = threading.Thread(name="client", target=client.run)

print("jest po stworzeniu")

client_thread.start()

window.run()

print("kot")
