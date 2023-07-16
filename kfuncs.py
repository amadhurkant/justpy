def removeData(remove, data):
    if remove not in data:
        raise Exception(f"RemoveNotError: Data to be removed- {remove} -not found in provided data")
    occurence = data.count(remove)
    if remove in data:
        data0 =  data.split(remove, occurence)
    data2 = ''
    for i in data0:
        data2 = data2+i
    return data2

def checkHx(hexdat, h=0):
    if h % 2 != 0:
        raise Exception("HexLengthError: The second argument must be a even number")
    int_test = int(hexdat, 16)
    if h > 0:
        if len(hexdat) > h:
            raise Exception("HexLengthExcept: Hex length is greater than input hex")
        else:
            res = hexdat.rjust(h, '0')
            return res
    else:
        if len(hexdat) % 2 == 0:
            return hexdat
        else:
            hexdat = "0"+hexdat
            return hexdat

def eugclidianGCDTable(a, b):
    if b > a:
        x = b
        p = a
        q, r = b // a, b % a
    else:
        x = a
        p = b
        q, r = a // b, a % b
    n = 0
    lister = [x, p, q, r]
    dicti = {
    n: lister
    }
    while True and lister[3]  != 0:
        lister = [lister[1], lister[3], lister[1]//lister[3], lister[1]%lister[3]]
        q, r, ra = p // r, r, p % r
        n += 1
        dicti[n] = lister
    return dicti
