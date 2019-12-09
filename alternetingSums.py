def alternatingSums(a):
    i=0
    sum=0
    sum1=0
    new=[]
    while i<len(a):
        if i%2==0:
            sum=sum+a[i]
        else:
            sum1=sum1+a[i]
        i=i+1
    new.append(sum)
    new.append(sum1)
    return new
alternatingSums([50, 60, 60, 45, 70])     