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

def checkHx(hexdat):
    if len(hexdat) % 2 == 0:
        return hexdat
    else:
        hexdat = "0"+hexdat
    return hexdat
