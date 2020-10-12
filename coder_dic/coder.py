from coder_dic.coder_setting import CoderSetting
import random


class Coder:
    def __init__(self, coder_setting: CoderSetting):
        self.random_bit_lenght = coder_setting.random_bit_lenght
        self.block_len = coder_setting.block_len

    def give_me_code_bin(self, message):
        string_to_list = []
        bit_list = []
        random_bits = [random.randrange(0, 2) for x in range(self.random_bit_lenght + 1)]
        random_bits[0] = 1
        random_bit_str = ""
        for bit in random_bits:
            random_bit_str += str(bit)
        for char in message:
            bit = bin(ord(char))[2:]
            for x in range(8 - len(bit)):
                bit = "0" + bit
            if len(bit) == 8:
                bit_list.append(bit)

        bit_coded_list = [random_bit_str]
        strin = ""
        for block in bit_list:
            for x in range(len(block)):
                if random_bits[x] == 1:
                    if block[x] == '1':
                        string_to_list.append('0')
                    else:
                        string_to_list.append('1')
                else:
                    if block[x] == '1':
                        string_to_list.append('1')
                    else:
                        string_to_list.append('0')
            for x in string_to_list:
                strin += x
            bit_coded_list.append(strin)
            string_to_list.clear()
            strin = ""
            # zakodowane bity w paczkach po 8
        return bit_coded_list

    def give_me_packed_code_bin(self, short_code):
        packed_code_list = []
        long_block = ""
        counter = 0
        for x in short_code:
            counter += 1
            long_block += x
            if counter == 4:
                packed_code_list.append(long_block)
                counter = 0
                long_block = ""
        to_cut = 4 - counter
        print("to cut ==", to_cut)
        last_block = ""
        if long_block != "":
            if to_cut == 3:
                last_block = "01000011"
            elif to_cut == 2:
                last_block = "01000010"
            elif to_cut == 1:
                last_block = "01000001"
        elif to_cut == 4:
            for x in range(5):
                long_block += "01000100"
        if to_cut != 4:
            for x in range(4 - counter):
                long_block += last_block
        packed_code_list.append(long_block)
        return packed_code_list

    def bin_to_int(self, bin_code):
        int_list = []
        print(bin_code)
        for x in bin_code:
            int_list.append(int(x, 2))
        return int_list

    def int_to_bin(self, int_code):
        bin_list = []
        for x in int_code:
            bin_list.append(bin(int(x))[2:])
        return bin_list

    def give_me_message(self, int_list):
        long_bin_list = self.int_to_bin(int_list)
        short_bin_list = []
        char_list = []
        for x in long_bin_list:
            for y in range(len(x) // 8):
                short_bin_list.append(x[y * 8:y * 8 + 8])
        random_code = short_bin_list[0]
        short_bin_list.pop(0)
        non_random_short_bin_list = []
        block_str = ""
        to_cut = 0
        for block in short_bin_list:
            for x in range(len(block)):
                if random_code[x] == '1':
                    if block[x] == '1':
                        block_str += '0'
                    else:
                        block_str += '1'
                else:
                    if block[x] == '1':
                        block_str += '1'
                    else:
                        block_str += '0'
            non_random_short_bin_list.append(block_str)
            block_str = ""
        last_block = short_bin_list[len(short_bin_list)-1]
        print("last block ==", last_block)
        if last_block == "01000011":
            to_cut = 3
        elif last_block == "01000010":
            to_cut = 2
        elif last_block == "01000001":
            to_cut = 1
        elif "01000100":
            to_cut = 4
        for x in non_random_short_bin_list:
            char_list.append(chr(int(x, 2)))
        message = ""
        for x in char_list:
            message += x
        print("to cut tuż przed napisanie wiadomosci ", to_cut)
        message = message[:-(to_cut)]
        return message

    def code_for_RSA(self, message):
        return self.bin_to_int(self.give_me_packed_code_bin(self.give_me_code_bin(message)))
