def countSwaps(a):
    i=0
    count=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[i]>a[j]:
                numSwaps=a[i]
                a[i]=a[j]
                a[j]=numSwaps
                count=count+1
            j=j+1
        i=i+1
    print "Array is sorted in %s swaps." % count
    print "First Element:", a[0]
    print "Last Element:", a[-1]
countSwaps([1,2,3])