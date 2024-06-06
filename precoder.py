import os
import sys
import random
import hamming


def butch(f_name):
    f = open(f_name, "rb")
    temp = f.read()
    # print(temp)
    temp = list(temp)
    # print(temp)
    return temp


def silck(fname, lstack):
    f = open(fname, "wb")
    for i in lstack:
        f.write(i.to_bytes(1, 'big'))


def max_size_show(f_name, deg):
    max_size = os.stat(f_name).st_size
    return ((max_size - 54) // 8) * deg


def LSBF(f_name, intstack, deg=1):
    it = 8 / deg
    text_mask, img_mask = create_mask_m(deg)
    f = open(f_name, 'rb')
    data54 = bytearray(f.read(54))
    max_size = maxsus(f_name, deg)
    # print(max_size)
    n = open('eggs.bmp', 'wb')
    n.write(data54)
    sosus = len(intstack)
    # print(sosus)
    lol = 0
    for i in range(max_size):
        huh = 0
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            temp1 = temp & img_mask
            inner = ((sosus * 2 << lol) & text_mask << (8 * max_size - 8)) >> (8 * max_size - deg)
            if temp1 != inner:
                # print(temp,inner)
                if random.choice([True, False]):
                    temp = temp + 1
                else:
                    temp = temp - 1
                # print("!",temp,inner)
            n.write(temp.to_bytes(1, 'big'))
            huh += 1
            lol += 1
    # print(sosus)
    sos = 0
    while sos < sosus:

        komik = hamming.sosisochka(hamming.ham(intstack[sos]))
        # print(hamming.ham(intstack[sos]))
        # print(sosus,sos,intstack[sos])
        biba = []
        boba = []
        for i in [0, 1]:
            huh = 0
            muh = 0
            komok = []
            sushka = []
            while huh < it:
                temp = int.from_bytes(f.read(1), 'big')
                sushka.append(temp)
                temp1 = temp & img_mask
                komok.append(temp1)
                huh += 1
            # print("Исходник: ",komok)
            somik = hamming.metadeham(komok, [0, 0, 0, 0, 0, 0, 0, 0])[0:4]
            # print("Синдром:  ",somik)
            # print("Внедрение:",komik[i])
            lama = hamming.cheburek(somik, komik[i]) + [0, 0, 0, 0]
            korj = hamming.metaham(lama)[0]
            # print(korj)
            # print(komok)
            korj = hamming.cheburek_big(korj, komok)
            # print(hamming.metadeham(korj,[0,0,0,0,0,0,0,0])[0:4])
            if i == 0:
                biba = korj
            else:
                boba = korj
            while muh < it:
                temp = sushka[muh]
                temp1 = temp & img_mask
                # print(temp1,korj[muh])
                # print(sushka[muh])
                if temp1 != korj[muh]:
                    if random.choice([True, False]):
                        sushka[muh] += 1
                        if sushka[muh] < 0:
                            sushka[muh] += 1
                    else:
                        sushka[muh] -= 1
                        if sushka[muh] < 0:
                            sushka[muh] += 1

                # print(sushka[muh],temp)
                # print(sushka[muh])
                n.write(sushka[muh].to_bytes(1, 'big'))
                muh += 1
            # print(hamming.metadeham(korj,[0,0,0,0,0,0,0,0])[0:4])
        # print(biba,boba,hamming.metadeham(biba,boba))
        # break
        sos += 1
        # print(mem)
    lastdata = bytearray(f.read())
    # print(sos)
    n.write(lastdata)


def LSBR(f_name, intstack, deg=1):
    it = 8 / deg
    text_mask, img_mask = create_mask(deg)
    f = open(f_name, 'rb')
    data54 = bytearray(f.read(54))
    max_size = maxsus(f_name, deg)
    # print(max_size)
    n = open('eggs.bmp', 'wb')
    n.write(data54)
    sosus = len(intstack)
    lol = 0
    for i in range(max_size):
        huh = 0
        # print(intstack[sos])
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            temp1 = temp & img_mask
            inner = ((sosus << lol * deg) & text_mask << (8 * max_size - 8)) >> (8 * max_size - deg)
            temp1 = temp1 | inner
            # print(bin(temp), bin(temp1), inner,sosus.to_bytes(max_size,'big'))
            n.write(temp1.to_bytes(1, 'big'))
            huh += 1
            lol += 1
    # print(sosus)
    sos = 0
    while sos < sosus:
        huh = 0
        # print(intstack[sos])
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            temp1 = temp & img_mask
            inner = ((intstack[sos] << huh * deg) & text_mask) >> (8 - deg)
            temp1 = temp1 | inner
            # print(temp,bin(temp), temp1,bin(temp1), inner,bin(inner))
            n.write(temp1.to_bytes(1, 'big'))

            huh += 1

        # print(temp)
        sos += 1
        # print(mem)
    lastdata = bytearray(f.read())
    # print(sos)
    n.write(lastdata)


def LSBM(f_name, intstack, deg=1):
    it = 8 / deg
    text_mask, img_mask = create_mask_m(deg)
    # print(bin(text_mask),bin(img_mask))
    f = open(f_name, 'rb')
    data54 = bytearray(f.read(54))
    max_size = maxsus(f_name, deg)
    n = open('eggs.bmp', 'wb')
    n.write(data54)
    sosus = len(intstack)
    lol = 0
    for i in range(max_size):
        huh = 0
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            temp1 = temp & img_mask
            inner = ((sosus << lol) & text_mask << (8 * max_size - 8)) >> (8 * max_size - deg)
            if temp1 != inner:
                # print(temp,inner)
                if random.choice([True, False]):
                    temp = temp + 1
                else:
                    temp = temp - 1
                # print("!",temp,inner)
            n.write(temp.to_bytes(1, 'big'))
            huh += 1
            lol += 1

    sos = 0
    while sos < sosus:
        huh = 0
        # print(intstack[sos])
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            temp1 = temp & img_mask
            inner = ((intstack[sos] << huh) & text_mask) >> (8 - deg)
            if temp1 != inner:
                if random.choice([True, False]):
                    temp = temp + 1
                else:
                    temp = temp - 1
            # print(temp, temp1, inner)
            n.write(temp.to_bytes(1, 'big'))
            huh += 1
        # print(temp)
        sos += 1
        # print(mem)
    lastdata = bytearray(f.read())
    n.write(lastdata)


def DLSBR(f_name, deg=1):
    it = 8 / deg
    text_mask, img_mask = create_mask(deg)
    f = open(f_name, 'rb')
    data54 = bytearray(f.read(54))
    max_size = maxsus(f_name, deg)
    red_mask = text_mask >> (8 - deg)
    sosus = 0
    lol = 0
    for i in range(max_size):
        huh = 0
        # print(intstack[sos])
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            sosus <<= deg
            temp1 = temp & red_mask
            sosus = (sosus | temp1)
            # print(temp1,sosus)
            # print(temp, temp1, inner,sosus.to_bytes(max_size,'big'))
            huh += 1
            lol += 1
    # sosus = int.from_bytes(sosus,'big')
    intstack = []
    # print(sosus)
    for i in range(sosus):
        huh = 0
        # print(intstack[sos])
        memo = 0
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            temp1 = temp & red_mask
            memo <<= deg
            memo = (memo | temp1)
            # print(temp, temp1, memo)
            huh += 1

        intstack.append(memo)
    return intstack


def DLSBF(f_name, deg=1):
    it = 8 / deg
    text_mask, img_mask = create_mask(deg)
    f = open(f_name, 'rb')
    data54 = bytearray(f.read(54))
    max_size = maxsus(f_name, deg)
    red_mask = text_mask >> (8 - deg)
    sosus = 0
    lol = 0
    for i in range(max_size):
        huh = 0
        # print(intstack[sos])
        while huh < it:
            temp = int.from_bytes(f.read(1), 'big')
            sosus <<= deg
            temp1 = temp & red_mask
            sosus = (sosus | temp1)
            # print(temp1,sosus)
            # print(temp, temp1, inner,sosus.to_bytes(max_size,'big'))
            huh += 1
            lol += 1

    # sosus = int.from_bytes(sosus,'big')
    # intstack = []
    print(sosus)


def create_mask(deg):
    text_mask = 0b11111111
    img_mask = 0b11111111

    text_mask <<= (8 - deg)
    text_mask %= 256
    img_mask >>= (deg)
    img_mask <<= (deg)

    return text_mask, img_mask


def create_mask_m(deg):
    text_mask = 0b11111111
    img_mask = 0b11111111

    text_mask <<= (8 - deg)
    text_mask %= 256
    img_mask >>= (8 - deg)

    return text_mask, img_mask


def maxsus(f_name, deg):
    i = 2
    n = 1
    while i ** (n - 1) < max_size_show(f_name, deg):
        # print(n,i ** (n - 1))
        n += 1
    i = 0
    while n > i * 8:
        i += 1
    return (i)


if __name__ == "__main__":
    # joj = butch("sos.txt")
    # print(butch("sos.txt"))
    # LSBR("6.bmp", butch("Better Mechanoid Loot continued.zip"), 1)
    # print("asd")
    # hoh = DLSBF("eggs.bmp",1)
    # silck(DLSBR("eggs.bmp",2))
    print(silck("eggs.zip", DLSBR("eggs.bmp")))
    # print(max_size_show("6.bmp",1))
    # text_mask,img_mask = create_mask(deg)
    # print(bin(text_mask),bin(img_mask))
