#!/usr/bin/python

# Opens lista and listb respectively as read only
A = open("lista.txt", "r")
B = open("listb.txt", "r")

listA = A.read().strip().splitlines()
# listA = ['d01', '2', '3', '4']
listB = B.read().strip().splitlines()
# listB = ['7', '6', '3']
# Result A - Only in A / Result B - Only in B / Result C - Both A and B/

ResultA = list(set(listA) - set(listB))
ResultB = list(set(listB) - set(listA))
ResultC = list(set(listA) & set(listB))

print('Only in A', ResultA)
print('Only in B', ResultB)
print('Both', ResultC)

# Closing both files
A.close()
B.close()
