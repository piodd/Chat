from user_interface.Window import Window
from client.client import Client
from encrypt.RSA import RSA
from coder_dic.coder import Coder
from coder_dic.coder_setting import CoderSetting


class Connector:
    def __init__(self, client: Client, window: Window):
        self.client = client
        self.window = window
        # user:[power,mod]
        self.dic_of_key = {}
        self.coder = Coder(CoderSetting())
        self.rsa = window.rsa
        self.is_safe_mode = window.is_safe_mode

    def client_to_window(self, message):
        print("client to window ==", message)
        self.prepared_message(message)
        pass

    def window_to_client(self, message):
        print("winodw_to_client===", message)
        self.client.send(message)

    def prepared_message(self, message: str):
        prepared_message = ""
        temp = ""
        if message[1] == '0':
            prepared_message = message[3:]
            self.window.add_message(message)
        elif message[1] == '1':
            temp = message[3:]
            temp = message.split(":", 2)[1]
            print("jestesmy po message[1]", message)
            print("temp2", temp[2], temp[2] == '0')
            if temp[2] == '2':
                temp = temp[2:]
                if temp[0] == '2':
                    self.this_is_for_me(temp[2:])
            elif temp[2] == '3':
                print("otrzymano klucz", temp)
                self.safe_new_key(temp)
            elif temp[2] == '4':
                print("wyslano klucz")
                self.send_key(self.window.user_name)
            elif temp[2] == '0':
                print("kots sie przywitał ")
                self.window.add_message(message.replace("-0-", ""))
        elif message[1] == '2':
            self.this_is_for_me(message)

    def say_hello(self):
        self.client.send("-0-" + "hello")

    def safe_new_key(self, message: str):
        list = message.split("-")
        temp = list[5]
        temp = temp.split("[")[1].replace("]", "").split(",")
        print("temp === po split ==", temp)
        power = temp[0]
        mod = temp[1]
        user = '1' + "-" + list[3]
        print("list w new key==", list)
        self.dic_of_key[user] = [int(power), int(mod)]
        print(self.dic_of_key)

    # first is 2
    def this_is_for_me(self, message):
        user_name = ""
        temp_list = message.split("-", 2)
        temp = temp_list[0] + "-" + temp_list[1]
        if self.window.user_name == temp:

            temp = temp_list[2]
            temp_list = temp.split("[", 1)
            user_name = temp_list[0]
            temp = temp_list[1]
            temp = temp.replace("]", "")
            temp_list = temp.split(",")
            int_list = []
            for x in temp_list:
                int_list.append(int(x))
            dec_list = []
            for x in int_list:
                dec_list.append(self.rsa.decryption(x))
            message = self.coder.give_me_message(dec_list)
            self.window.add_message(user_name + " : " + message)
            # dekodowanie tutaj
        else:
            pass

    def send_safe(self, user, message):
        if not (user in self.dic_of_key):
            print("wysłano prosbe")
            self.send_ask_for_key(user)
        list_rsa = []
        # print(" ")
        # print("==================================================")
        #  print("message==", message)
        code = self.coder.code_for_RSA(message)
        # print("==================================================")
        # print("w send safe====", code)
        public_power = self.dic_of_key[user][0]
        mod = self.dic_of_key[user][1]
        temp_rsa = RSA(public_power, 1, mod)
        for x in code:
            list_rsa.append(temp_rsa.encryption(x))
        prepered_to_send = list_rsa
        #  print(prepered_to_send)
        # print("user=======", user)
        #  print("to co leci do clienta", "-2-" + user + "-" + self.window.user_name + str(prepered_to_send))
        # 2 is safe message
        self.client.send("-2-" + user + "-" + self.window.user_name + str(prepered_to_send))

    def send_key(self, user):
        keys = "[" + str(self.rsa.public_key_power) + "," + str(self.rsa.mod) + "]"
        self.client.send("-3-" + user + "-" + self.window.user_name + keys)

    def send_ask_for_key(self, user):
        if user in self.dic_of_key:
            pass
        else:
            self.client.send("-4-" + user + "-" + self.window.user_name)
