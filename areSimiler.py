def areSimilar(a, b):
    result=False
    for i in a:
        for j in b:
            if i == j and i in b:
                result= True
            else:
                result = False 
    return result    
areSimilar([1, 2, 3],[1, 2, 3])