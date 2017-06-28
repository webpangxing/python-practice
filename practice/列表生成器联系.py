from collections import Iterable #引入collections模块，验证是否支持迭代
print  (isinstance('abc',Iterable))


#[4, 16, 36, 64, 100]
list1 = [x * x  for x in range(1,11) if x % 2 == 0]
print(list1)

#使用两层循环，生成全排列['AX', 'AY', 'BX', 'BY']
str = [m + n for m in 'AB' for n in 'XY']
print(str)