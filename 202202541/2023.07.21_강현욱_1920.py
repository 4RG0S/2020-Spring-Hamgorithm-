import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000) 
#����Ž��
def binary(start, end,array, target):
    mid=(start+end)//2
    if start>end:
        print(0)
        return 0
    if array[mid]==target:
        print(1)
        return 0
    elif target>array[mid]:
        return binary(mid+1,end,array,target)
    elif target<array[mid]:
        return binary(start, mid-1,array, target)
#ã��
x=int(input())
ls=[]
ls1=[]
ls=list(map(int,input().split()))
y=int(input())
ls1=list(map(int,input().split()))
ls.sort()
for q in range(y):
    binary(0,x-1,ls,ls1[q])
