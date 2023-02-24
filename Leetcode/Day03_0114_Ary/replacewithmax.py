#Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1. After doing so, return the array.
def replacewithmax(arr: list[int]):
        #initialmax =-1
        #reverse iteration
        #new max = max(oldmax,arr[i])

        rightmax= -1
        for i in range(len(arr)-1,-1,-1):
            newmax =max(rightmax,arr[i]) 
            arr[i] =rightmax #replace current element with right max
            rightmax= newmax #replace rightmax with new max
        return arr
            #(last element, iterate in reverse so -1 and stop once at the beg so -1)
arr=[17,18,5,6,4,1]
print(replacewithmax(arr))