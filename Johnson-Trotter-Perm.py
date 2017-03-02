sMyList = '0123'
iList = [[int(item), -1] for item in sMyList]
k = n = 0

def getmobile():
    global k, iList
    ret = False
    j = 0
    for i in range(len(iList)):
        pointing_index = i + iList[i][1]
        if 0 <= pointing_index < len(iList):
            if iList[i][0] > iList[pointing_index][0]:
                if not ret:
                    ret = True
                    j = i
                elif iList[i][0] > iList[j][0]:
                    j = i
    k = j
    return ret


def swap():
    global k, iList
    dir = iList[k][1]
    tmp = iList[k + dir]
    iList[k + dir] = iList[k]
    iList[k] = tmp


def reverse():
    global k, iList
    for i in range(len(iList)):
        if iList[i][0] > iList[k][0]:
            iList[i][1] *= -1


print(n, iList)
n += 1
if getmobile():
    swap()
    print(n, iList)
    n += 1
while getmobile():     # k: index of largest mobile
    reverse()
    swap()
    print(n, iList)
    n += 1
