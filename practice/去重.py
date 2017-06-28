# list 去重
def remove_duplicates(lists):
    list1 = []
    for i in lists:
        if not (i in list1):
            list1.append(i)
    print(list1)
    return list1

remove_duplicates([1,5,3,4,1,3,7,2,6,9,6])

