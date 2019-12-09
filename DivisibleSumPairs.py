a=[1 ,3 ,2 ,6 ,1 ,2]
n=len(a)
k=3
i=0
new_list=[]
count=0
while i<len(a):
    j=i+1
    while j<len(a):
        sum=a[i]+a[j]
        if sum%k==0:
            new_list.append([a[i],a[j]])
            count=count+1
        j=j+1
    i=i+1
print new_list
print count