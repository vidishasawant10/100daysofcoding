#Implement a function findMinimum(lst) which finds the smallest number in the given list.
def find_minimum(arr):
    mini=arr[0]
    for i in arr:
        if i < mini:
            mini=i
    return mini
    # Write your code here
    pass

arr=[3,5,2,3,6,8]
print(find_minimum(arr))