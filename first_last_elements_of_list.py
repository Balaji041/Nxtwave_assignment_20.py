N=int(input())
l=[]
for i in range(N):
    num=int(input())
    if i<2 or i>(N-3):
        l+=[num]
print(l)

"""
input:5
1
11
13
21
19
output:[1, 11, 21, 19]
"""
