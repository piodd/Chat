import tkinter as tk
from user_interface.setting import Setting
from encrypt.RSA import RSA
from encrypt import key_generator


class LoginWindow:
    def __init__(self, setting: Setting):
        self.setting = setting
        self.counter = 0
        self.message_list = []
        self.window = tk.Tk()
        self.frame = tk.Frame(self.window)

        # label user_name
        self.frame.grid(row=0, column=0, columnspan=1, rowspan=1)
        self.user_name_label = tk.Label(master=self.frame, text="USERNAME")
        self.user_name_label.pack()

        # enter user_name

        self.frame.grid(row=1, column=1)
        self.text_to_send = tk.Entry(self.frame)
        self.text_to_send.pack()

        # button to confirmed

        self.frame.grid(row=2, column=0, columnspan=2)
        self.button_send = tk.Button(self.frame, command=self.confirmed, text="LOG IN")
        self.button_send.pack()

        # button to confirmed

        self.frame.grid(row=3, column=0, columnspan=2)
        self.button_send = tk.Button(self.frame, command=self.confirmed_safe, text="LOG IN SAFE MODE")
        self.button_send.pack()

        self.window.mainloop()

    def confirmed(self):
        self.setting.user_name = "0-" + self.text_to_send.get()
        self.window.destroy()

    def confirmed_safe(self):
        # create private and public key and create class RSA
        keys = key_generator.give_me_new_keys()
        gen_keys = key_generator.key_generator(keys[0], keys[1])
        public_power = gen_keys[0]
        public_mod = gen_keys[1]
        private_key = gen_keys[2]
        rsa = RSA(public_power, private_key, public_mod)
        print(gen_keys)
        # first number is 0/1 and that means safe mode on/off next number is public power and public mod(public keys )
        self.setting.user_name = "1-"+ self.text_to_send.get()
        self.setting.set_RSA(rsa=rsa)
        self.window.destroy()
