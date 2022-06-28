def bubble(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li
print(bubble([10,3,2,14,5,6,34,2,1]))