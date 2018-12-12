import random


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
        else:
            flag = True
    return flag


def generate_prime():
    prime_list = []
    for i in range(50, 100):
        if prime(i):
            prime_list.append(i)
    return random.sample(prime_list, 2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def generate_d(e, fn):
    for d1 in range(fn):
        x = (e*d1) % fn
        if x == 1:
            d = d1
            break
    return d


def generate_key(p, q):
    e_list = []
    n = p*q
    fn = (p-1)*(q-1)
    for e in range(50, 150):
        if gcd(fn, e) == 1:
            e_list.append(e)
    e = random.choice(e_list)
    d = generate_d(e, fn)
    return (e, n), (d, n)


def encrypt(m, nl, e, n):
    num_list = []
    encrypt_num_list = []
    for i in range(0,len(m),nl-1):
        if i+nl-1 < len(m):
            num = m[i:i+nl-1]
        else:
            num = m[i:]
        num_list.append(int(num))
    for num in num_list:
        encrypt_num = pow(num, e) % n
        encrypt_num_list.append(str(encrypt_num))
    # for encrypt_num in encrypt_num_list:
    #     print(encrypt_num)
    password = "".join(encrypt_num_list)
    return encrypt_num_list,password


def decrypt(encrypt_list, d, n):
    decrypt_num_list = []
    for num in encrypt_list:
        # print(num)
        encrypt_num = pow(int(num), d) % n
        decrypt_num_list.append(str(encrypt_num))
    message = "".join(decrypt_num_list)
    return message


if __name__ == '__main__':
    p, q = generate_prime()
    print("随机产生素数p的值为:%d\n随机产生素数q的值为:%d"%(p, q))
    (e, n), (d, n) = generate_key(p, q)
    print("e:%d,  d:%d,  n:%d"%(e, d, n))
    message = input("请输入您想加密的数字:")
    encrypt_list, password = encrypt(message, len(str(n)), e, n)
    print("产生的密码值为:%s" % password)
    f_message = decrypt(encrypt_list, d, n)
    print("最终解密的明文值为:%s" % f_message)


