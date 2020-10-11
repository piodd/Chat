class RSA:
    def __init__(self, public_key_power, private_key, mod):
        self.private_key = private_key
        self.public_key_power = public_key_power
        self.mod = mod

    def calculate_mod_power(self, number, mod, power):
        bin_form = bin(power)
        list_of_power = []
        list_of_value = [number]
        result = 1

        for x in bin_form[2:]:
            list_of_power.append(int(x))
        list_of_power.reverse()

        for x in range(1, len(list_of_power)):
            next_value = (list_of_value[x - 1] ** 2) % mod

            list_of_value.append(next_value)
        for x in range(len(list_of_power)):
            if list_of_power[x] == 1:
                result = (result * list_of_value[x]) % mod
        return result

    def encryption(self, message):
        result = self.calculate_mod_power(message, self.mod, self.public_key_power)
        return result

    def decryption(self, message):
        result = self.calculate_mod_power(message, self.mod, self.private_key)
        return result

    def encryption_to_someone(self, message, mod, public_key_power):
        return self.calculate_mod_power(message, mod, public_key_power)
