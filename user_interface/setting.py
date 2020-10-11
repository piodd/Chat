from encrypt.RSA import RSA


class Setting:
    def __init__(self, title="chat", height=600, width=600, user_name=""):
        self.user_name = user_name
        self.title = title
        self.height = height
        self.width = width
        self.rsa = None
        self.is_safe_mode = False

    def set_RSA(self, rsa: RSA):
        self.is_safe_mode = True
        self.rsa = rsa
