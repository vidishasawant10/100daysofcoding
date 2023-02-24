#Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).
def merge_lists(lst1, lst2):
    indx1=0
    indx2=0
    while (indx1<len(lst1)and indx2<len(lst2)):
        if lst1[indx1] > lst2[indx2]:
            lst1.insert(indx1,lst2[indx2])
            indx1+=1
            indx2 +=1
        else:
            indx1+=1

    if indx2 <len(lst2):
        lst1.extend(lst2[indx2:])
    return lst1
    # Write your code here
    pass
lst1 = [1,3,4,5]  
lst2 = [2,6,7,8]
print(merge_lists(lst1,lst2))