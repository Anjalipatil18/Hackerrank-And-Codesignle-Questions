def addBorder(picture):
    a=[]
    for i in picture:
        s="*" + i + "*"
        a.append(s)
        length=len(s)
        k="*" * length
    a.append(k)
    a.insert(0, k)
    return a
addBorder(["abc", "ded"])

    