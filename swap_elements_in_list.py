L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

#Write your code here
l1=int(input())
l2=int(input())
l1_vales=L[l1]
l2_vales=L[l2]
L[l2]=l1_vales
L[l1]=l2_vales
print(L)

"""
input:2
6
output:[1, 'two', 'four', 5.09, 'Three', -558, 9, -93.7, 'six']

"""
