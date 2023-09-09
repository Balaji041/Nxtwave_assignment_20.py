N=int(input())
T=int(input())
l=[]
for i in range(N):
    num=int(input())
    l+=[num]
for i in range(T):
    num=int(input())
    li=l[num]
    print(li)
"""
input:4
2
1
2
3
4
0
3
output:
1
4

"""
