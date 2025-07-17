L = [4,5,-6,-9,109048843884248,-834857858478957834973919874,0.000000000000000000000000000000001]
print("original list:", L)

count = 0
for i in L:
    count += 1
print("number of elements in the list:", count)

avg = count / len(L)

print("average of the list:", avg)
print("sum of the list:", sum(L))
print("maximum of the list:", max(L))
print("minimum of the list:", min(L))