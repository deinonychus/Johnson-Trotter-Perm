sMyList = '0123'
iList = [[int(item), -1] for item in sMyList]
k = 0

def getmobile(iList):
    global k
    ret = False
    for i in range(len(iList)):
        pointing_index = i + iList[i][1]
        if 0 <= pointing_index < len(iList):
            if iList[i][0] > iList[pointing_index][0]:
                if not ret:
                    ret = True
                    k = i
                elif iList[i][0] > iList[ret][0]:
                    k = i
    return ret


def swap():
    global k
    dir = iList[k][1]
    tmp = iList[k + dir]
    iList[k + dir] = iList[k]
    iList[k] = tmp


def reverse():
    global k
    for i in range(len(iList)):
        if iList[i][0] > iList[k][0]:
            iList[i][1] *= -1


print(iList)
while getmobile(iList):     # k: index of largest mobile
    swap()
    if getmobile(iList):
        reverse()
        print(iList)
    else:
        print(iList)
        break
