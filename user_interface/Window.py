import tkinter as tk
from user_interface.setting import Setting


class Window:
    def __init__(self, setting: Setting):
        self.counter = 0
        self.message_list = []
        self.window = tk.Tk()

        self.frame = tk.Frame(self.window)

        # text box for chat massage
        self.frame.grid(row=0, column=0, columnspan=2, rowspan=3, padx=200, pady=200)
        self.chat_text = tk.Text(master=self.frame)
        self.chat_text.insert(tk.INSERT, "WELCOME: " + setting.user_name + "\n")
        self.chat_text.pack()

        # enter box to send

        self.frame.grid(row=3, column=1)
        self.text_to_send = tk.Entry(self.frame)
        self.text_to_send.pack()

        # button to send

        self.frame.grid(row=3, column=0)
        self.button_send = tk.Button(self.frame, command=self.send, text="SEND")
        self.button_send.pack()

        self.user_name = setting.user_name

        # chosen user 
        self.frame.grid(row=3, column=2)
        self.button_chosen = tk.Button(self.frame, command=self.set_choose_user, text="chose user")
        self.button_chosen.pack()

        self.chosen_user = ""

        # enter chosen

        self.frame.grid(row=3, column=2)
        self.text_chosen = tk.Entry(self.frame)
        self.text_chosen.pack()
        # say hello
        self.frame.grid(row=3, column=3)
        self.say_hello = tk.Button(self.frame, command=self.say_hello, text="say hello")
        self.say_hello.pack()

        # chosen_user

        self.chosen_user = ""

        # client
        self.connector = None
        self.rsa = setting.rsa
        self.is_safe_mode = setting.is_safe_mode

    def say_hello(self):
        self.connector.say_hello()

    def set_choose_user(self):
        self.chosen_user = self.text_chosen.get()
        self.connector.send_ask_for_key(self.chosen_user)

    def run(self):
        self.window.mainloop()

    def import_connector(self, connector):
        from client.connector import Connector
        self.connector = connector

    def send(self):
        message = self.text_to_send.get()
        self.text_to_send.delete(0, "end")
        self.message_list.append(message)
        if self.is_safe_mode:
            self.send_safe(message)
        else:
            self.connector.window_to_client(message)

    def send_safe(self, message):
        self.connector.send_safe(self.chosen_user, message)
        self.connector.send_safe(self.user_name, message)

    def add_message(self, message: str):
        self.message_list.append(message)
        self.chat_text.insert(tk.INSERT, message + "\n")
