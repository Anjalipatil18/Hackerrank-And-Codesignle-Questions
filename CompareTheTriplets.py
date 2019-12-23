def compareTriplets(a, b):
    i=0
    j=0
    s=0
    list=[]
    while i<len(a):
        if a[i]<b[j]:
            result=1
        if a[i]>b[j]:
            temp=1
            s=s+temp
        if a[i]==a[j]:
            k=1
        j=j+1
        i=i+1
    list.append(s)
    list.append(result)
    return list
compareTriplets([17, 28, 30],[99, 16, 8])