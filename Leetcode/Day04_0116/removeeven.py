#Implement a function that removes all the even elements from a given list. Name it remove_even(lst).
def remove_even(lst):
    res=[]
    for i in lst:
        if i%2!=0:
            res.append(i)
            i+=1

    return res
lst=[1,2,3,4,5,6,7,8]
print(remove_even(lst))