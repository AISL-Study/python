import math

def miniMaxSum(arr):
    Min=sum(arr)-max(arr)
    Max=sum(arr)-min(arr)
    print(Min , Max)

if __name__=="__main__":
    arr=list(map(int,input().rstrip().split()))
    miniMaxSum(arr)