import math
arr=input("enter the arrray").split(',')
arr=list(map(int,arr))
key=int(input("enter the key to be found"))
low=0
high=len(arr)
def compute(x,y):
    if x==y:
        return 0
    elif x>y:
        return 1
    else :
        return -1

while low<=high:
    mid=math.floor((low+high)/2)
    if compute(key,arr[mid])==0:
        print("key is found at position ",mid)
        break
    elif compute(key,arr[mid])==1:
        low=mid+1
    else:
        high=mid-1