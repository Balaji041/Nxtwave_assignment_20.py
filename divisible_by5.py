N=int(input())
l=[]
for i in range(N):
    num=int(input())
    if num%5==0:
        l+=[num]
print(l)

"""
input:3
10
7
35
output:[10, 35]
"""
