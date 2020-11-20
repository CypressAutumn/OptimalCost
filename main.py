'''
    在工业生产中需要生产一种物料，可以有N种原材料组合，计算如何组合生产成本最低
'''

import itertools
import operator
#规格列表
list1 = [1, 2, 3, 4, 5,1, 2, 3, 4, 5]
#成本与规格列表
costList = {1:3.5, 2:4.0, 3:4.7, 4:5.01, 5:6.0}

#列出2到4层的任意组合
secLayer = list(itertools.combinations(list1, 2))
thrLayer = list(itertools.combinations(list1, 3))
forLayer = list(itertools.combinations(list1, 4))
fivLayer = list(itertools.combinations(list1, 5))

allLayer = secLayer + thrLayer + forLayer + fivLayer
#print(allLayer)
#print(sum(allLayer[10]))

ok_group = []
cost_group = []

for item in allLayer:
    if sum(item) == 10:
        ok_group.append(item)

#print('符合条件的组合数：',len(ok_group))


#迭代符合条件的组合计算成本
for group in ok_group:
    cost = []
    for ite in group:
        cost.append(costList[ite])
    cost_group.append(sum(cost))

min_index, min_number = min(enumerate(cost_group), key=operator.itemgetter(1))
print('最组合成本：', min_number, '组成为：', ok_group[min_index])

