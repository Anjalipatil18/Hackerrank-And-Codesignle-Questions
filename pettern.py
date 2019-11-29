t

# n = 15
# i=0
# while i<5:
#     j=0
#     while j<i+1:
#         print (n, end=" ")
#         n=n-1
#         j=j+1
#     print("\n")
#     i=i+1

# num=6
# for i in range(num):
#     for j in range((num-i)-1):
#         print(end=" ")
#     for j in range(65, 65+i):
#         a = chr(j)
#         print (a,end=" ")
#     print ()

# num=6
# for i in range(num):
#     for j in range((num - i) - 1):
#         print(end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# num=6
# i=0
# while i<num:
#     j=0
#     j=((num-i)-1)
#     print (end=" ")
#     j=65
#     while j<65+i:
#         a=chr(j)
#         print(a,end=" ")
#     print("\n")

num=6
i=0
while i<num:
    for j in range((num-i)-1):
        print(end=" ")
    j=65
    while j<65+i:
        a=chr(j)
        print(a,end=" ")
        j=j+1
    print("\n")
    i=i+1

#################################################################################################
n = 15
i=0
while i<5:
    j=0
    while j<i+1:
        print (n, end=" ")
        n=n-1
        j=j+1
    print("\n")
    i=i+1
    
num=6
i=1
while i<num:
    for j in range((num-i)-1):
        print(end=" ")
    j=65
    while j<65+i:
        a=chr(j)
        print(a,end=" ")
        j=j+1
    print("\n")
    i=i+1

num=6
for i in range(num):
    for j in range((num-i)-1):
        print(end=" ")
    for j in range(65, 65+i):
        a = chr(j)
        print (a,end=" ")
    print ("\n")