import itertools
import operator

class optimalCost:
    
    def __init__(self, tarLand, layerScope, error):
        #物料列表：规格（mm）：价格（x.00）
        #self.materiel = {}
        #规格列表
        self.specList = []
        #胶合板目标厚度
        self.tarLand = tarLand
        #物料的最小层数 最大组层数(4,5)
        self.layerScope = layerScope
        #允许正负误差
        self.error = error
    
    #计算组合
    def compose(self, materiel):
        #self.materiel = {2:5.1, 3:6.2, 1:3.7, 6:8.9}
        self.specList = self.makeSpecList(materiel)
        #用于存储所有组合
        allGroup = []
        #符合条件的组合
        goodGroup = []
        #最大层数+1才可以使range(2,maxNum)正确迭代
        maxNum = self.layerScope[1] + 1
        minNum = self.layerScope[0]
        #生成所有组合
        for i in range(minNum,maxNum):
            allGroup = allGroup + list(itertools.combinations(self.specList, i))
        max_error = self.tarLand + self.error
        min_error = self.tarLand - self.error
        #计算符合条件的组合
        for item in allGroup:
            if sum(item) <= max_error and sum(item) >= min_error:
                goodGroup.append(item)
        #去除重复
        goodGroup = list(set(goodGroup))
        return goodGroup
    
    #获取最优组合列表
    def optimalGroup(self, materiel):
        #存储成本组合字典
        costGroup = {}
        #迭代符合条件的组合
        for group in self.compose(materiel):
            #临时存储费用
            cost = []
            for item in group:
                cost.append(materiel[item])            
            costGroup[group] = (round(sum(cost),2))
        #排序
        costGroup = sorted(costGroup.items(), key=operator.itemgetter(1))
        return self.popOver(costGroup)
    
    #去重
    def popOver(self, costGroup):
        temp = []
        for it in costGroup:
            temp.append([set(it[0]), it[1]])
        group_len = len(temp)
        index_group = []
        for i in range(0,group_len):
            w = i+1
            if w < group_len:
                if temp[i] == temp[w]:
                    index_group.append(i)
        index_group.sort(reverse = True)
        for i in index_group:
            costGroup.pop(i)
        
        temp = []
        for it in costGroup:
            temp.append([set(it[0]), it[1]])
        group_len = len(temp)
        index_group = []
        for i in range(0,group_len):
            w = i+2
            if w < group_len:
                if temp[i] == temp[w]:
                    index_group.append(i)
        index_group.sort(reverse = True)
        for i in index_group:
            costGroup.pop(i)
        return costGroup



        
        
    
    #生成规格数组用于计算组合
    def makeSpecList(self, materiel):
        oneList = []
        twoList = []
        for item in materiel:
            oneList.append(item)
        #根据规格个数横向复制相应倍数，确保组合中没有疏漏
        for i in range(0, len(oneList)):
            twoList = twoList + oneList
        return twoList