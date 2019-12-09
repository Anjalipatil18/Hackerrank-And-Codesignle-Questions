def adjacentElementsProduct(inputArray):
    i=0
    new_list=[]
    j=i+1
    while j<len(inputArray):
        multiple=inputArray[i]*inputArray[j]
        new_list.append(multiple)
        j=j+1
        i=i+1
    index=0
    maximum=new_list[index]
    while index<len(new_list):
        if  new_list[index]>maximum:
            maximum=new_list[index]
        index=index+1
    return maximum
print adjacentElementsProduct([-23, 4, -3, 8, -12])