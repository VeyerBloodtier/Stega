def ham(kod):
    out = []
    while kod != 1:
        out.append(kod % 2)
        kod = kod // 2
    out.append(1)
    while len(out) < 8:
        out.append(0)
    return out
    # out.reverse()
    # print(out)


def deham(sqr):
    out = 0
    h = 0
    for i in sqr:
        out += i * 2 ** h
        # print(2**h,out)
        h += 1
    # print(out)
    return out


def sosisochka(sqrt):
    al = sqrt[0:4]
    ar = sqrt[4:8]
    return al, ar


def desosisochca(sqrt1, sqrt2):
    return sqrt1 + sqrt2


def cheburek(sqrt1, sqrt2):
    out = [0, 0, 0, 0]
    for i in range(len(sqrt1)):
        if sqrt1[i] == sqrt2[i]:
            out[i] = 0
        else:
            out[i] = 1
    return out


def cheburek_big(sqrt1, sqrt2):
    out = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(sqrt1)):
        if sqrt1[i] == sqrt2[i]:
            out[i] = 0
        else:
            out[i] = 1
    return out


def metaham(sqrt):
    al = sqrt[0:4]
    ar = sqrt[4:8]
    out1 = [0, 0, 0, 0, 0, 0, 0, 0]
    out2 = [0, 0, 0, 0, 0, 0, 0, 0]

    out1[2] = al[0]
    out1[4] = al[1]
    out1[5] = al[2]
    out1[6] = al[3]
    out1[0] = (out1[2] + out1[4] + out1[6]) % 2
    out1[1] = (out1[2] + out1[5] + out1[6]) % 2
    out1[3] = (out1[4] + out1[5] + out1[6]) % 2

    out2[2] = ar[0]
    out2[4] = ar[1]
    out2[5] = ar[2]
    out2[6] = ar[3]
    out2[0] = (out2[2] + out2[4] + out2[6]) % 2
    out2[1] = (out2[2] + out2[5] + out2[6]) % 2
    out2[3] = (out2[4] + out2[5] + out2[6]) % 2

    return out1, out2


def metadeham(L, R):
    out1 = [0, 0, 0, 0, 0, 0, 0, 0]
    out2 = [0, 0, 0, 0, 0, 0, 0, 0]

    out1[2] = L[2]
    out1[4] = L[4]
    out1[5] = L[5]
    out1[6] = L[6]
    out1[0] = (L[2] + L[4] + L[6]) % 2
    out1[1] = (L[2] + L[5] + L[6]) % 2
    out1[3] = (L[4] + L[5] + L[6]) % 2

    if out1[0] == L[0]:
        a = 0
    else:
        a = 1
    if out1[1] == L[1]:
        b = 0
    else:
        b = 1
    if out1[3] == L[3]:
        c = 0
    else:
        c = 1
    out1[a * 1 + b * 2 + c * 4 - 1] = (out1[a * 1 + b * 2 + c * 4 - 1] + 1) % 2

    out2[2] = R[2]
    out2[4] = R[4]
    out2[5] = R[5]
    out2[6] = R[6]
    out2[0] = (R[2] + R[4] + R[6]) % 2
    out2[1] = (R[2] + R[5] + R[6]) % 2
    out2[3] = (R[4] + R[5] + R[6]) % 2

    if out2[0] == R[0]:
        a = 0
    else:
        a = 1
    if out2[1] == R[1]:
        b = 0
    else:
        b = 1
    if out2[3] == R[3]:
        c = 0
    else:
        c = 1

    out2[a * 1 + b * 2 + c * 4 - 1] = (out2[a * 1 + b * 2 + c * 4 - 1] + 1) % 2

    out = [out1[2], out1[4], out1[5], out1[6], out2[2], out2[4], out2[5], out2[6]]
    return out


if __name__ == "__main__":
    sos = ham(228)
    print("sos:", sos)
    coc = metaham(sos)
    print("coc:", coc)
    # coc[0][0] = 1
    coc[0][2] = 1
    print("coc[0]:", coc[0])
    sos = deham(coc[0])
    # print(sos)
    sos = deham(coc[1])
    # print(sos)
    sos = metadeham(coc[0], coc[1])
    print("sos:", sos)
    print(deham(sos))
