from encrypt import prime_number
import random


def find_divider(n):
    divider_list = []
    print(n)
    f = int(n ** (1 / 2))
    if n < 10000:
        for x in range(2, n):
            if n % x == 0:
                divider_list.append(x)
        return divider_list
    else:
        for x in range(2, f):
            if n % x == 0:
                divider_list.append(x)
                if len(divider_list) > 30:
                    return divider_list
        return divider_list


def key_generator(p, q):
    print("moje mod", p * q, p, q)
    group_size = (p - 1) * (q - 1)
    divider = find_divider(group_size + 1)
    good_key = False
    r = random.randrange(len(divider))
    private_key = divider[r]
    public_power_key = (group_size + 1) // private_key
    return [public_power_key, p * q, private_key]


def give_me_new_keys():
    is_good_key = False
    while not is_good_key:
        p = prime_number.prime_example()
        q = prime_number.prime_example()
        if p != q:
            is_good_key = True
    return [p, q]
