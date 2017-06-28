def median(lists):
    lists = sorted(lists)
    length = len(lists)
    middle = 0
    if length % 2 == 0:
        middle = (lists[int(length * 0.5 - 1)] + lists[int(length * 0.5)]) / 2.0
    else:
        middle = lists[int((length + 1) / 2 - 1)]
    print(middle)
    return middle
median([1,7,3,5])