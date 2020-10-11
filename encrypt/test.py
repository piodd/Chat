from encrypt import prime_number
from encrypt import key_generator
from encrypt.RSA import RSA

print(prime_number.give_me_primes_faster(1000 * 3))
keys = key_generator.give_me_new_keys()
gen_keys = key_generator.key_generator(keys[0], keys[1])
print(gen_keys)

public_power = gen_keys[0]
public_mod = gen_keys[1]
private_key = gen_keys[2]

encrypere = RSA(public_power, private_key, public_mod)

test_mess = 11111
dec = encrypere.decryption(test_mess)
enc = encrypere.encryption(dec)
print("przed zaszyfrowaniem==", test_mess)
print("po zaszyfrowaniu==", dec)
print("po deszyfracji == ", enc)
test_mess = test_mess + 1
dec = encrypere.decryption(test_mess)
enc = encrypere.encryption(dec)
print("przed zaszyfrowaniem==", test_mess)
print("po zaszyfrowaniu==", dec)
print("po deszyfracji == ", enc)
