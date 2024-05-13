def flatten(x):
    if isinstance(x, list):
        temp = []
        for piece in x:
            temp.extend(flatten(piece))
        return temp
    else:
        return [x]
    
    
def nested_reverse(input_list):
    if type(input_list) == list:
        return [nested_reverse(x) for x in input_list[::-1]]
    else:
        return input_list
 
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
res = flatten(liste)
             
print ("Düzleştirilmiş liste: " + str(res))

liste = [[1, 2], [3, 4], [5, 6, 7]]
print(nested_reverse(liste))

