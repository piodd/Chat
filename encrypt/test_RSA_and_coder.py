from encrypt.RSA import RSA
from coder_dic.coder import Coder
from coder_dic.coder_setting import CoderSetting
from encrypt import prime_number
from encrypt import key_generator

coder = Coder(CoderSetting())
keys = key_generator.give_me_new_keys()
gen_keys = key_generator.key_generator(keys[0], keys[1])
public_power = gen_keys[0]
public_mod = gen_keys[1]
private_key = gen_keys[2]

rsa = RSA(public_power, private_key, public_mod)
start_message = "ala ma kota i wgl spoko hahah elo leo 3 dwa zero a tak wgl to moze dziala "
code_block_8 = coder.give_me_code_bin(start_message)
packed_block = coder.give_me_packed_code_bin(code_block_8)
int_list_b = coder.bin_to_int(packed_block)

enrypted_list = []
decrypted_list = []
for x in int_list_b:
    enrypted_list.append(rsa.encryption(x))
print(enrypted_list)

for x in enrypted_list:
    decrypted_list.append(rsa.decryption(x))
print(decrypted_list)

message = coder.give_me_message(decrypted_list)

print(message,
      "////a na początku było 3 ostatnie znaki moga byc złe wynika to z niedopracowanego jeszcze kodowania //// ",
      start_message)

start_message = "kot"
code_message = coder.code_for_RSA(start_message)
enrypted_list.clear()
decrypted_list.clear()
for x in code_message:
    enrypted_list.append(rsa.encryption(x))

for x in enrypted_list:
    decrypted_list.append(rsa.decryption(x))
message = coder.give_me_message(decrypted_list)
print("druga próba ",message)
