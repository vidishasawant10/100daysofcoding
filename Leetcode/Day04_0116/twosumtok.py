#In this problem, you have to implement the find_sum(lst,k) function which will take a number k as input and return two numbers that add up to k.

def find_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] +lst[j] is k and i is not j:
                return [lst[i],lst[j]]
    # Write your code here
    pass

lst = [1,21,3,14,5,60,7,6]
k = 81
print(find_sum(lst,k))