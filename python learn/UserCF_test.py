# coding=utf-8


from math import sqrt
import random

# fp = open(r"test.txt", "r")

users = {}

for line in open("ilearn_data"):
    lines = line.strip().split(",")
    if lines[0] not in users:
        users[lines[0]] = {}
        # print(users)
    users[lines[0]][lines[2]] = float(lines[1])
    # print(users)


# ----------------新增代码段END----------------------



class recommender:
    # data：数据集，这里指users
    # k：表示得出最相近的k的近邻
    # metric：表示使用计算相似度的方法
    # n：表示推荐book的个数
    def __init__(self, data, k=5, metric='pearson', n=12):

        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}

        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson
        if type(data).__name__ == 'dict':
            self.data = data

    def ProductID2name(self, id):

        if id in self.productid2name:
            return self.productid2name[id]
        else:
            return id

            # 定义的计算相似度的公式，用的是皮尔逊相关系数计算方法

    def pearson(self, R1, R2):
        sum_P = 0
        sum_R1 = 0
        sum_R2 = 0
        sum_R1sq = 0
        sum_R2sq = 0
        n = 0

        for k in R1:
            if k in R2:
                n += 1
                x = R1[k] # x是当前用户学习过的课程的评分
                y = R2[k] # y是其他用户学习过的课程的评分
                sum_P += x * y #求乘积的和
                sum_R1 += x #对当前用户所有偏好求和
                sum_R2 += y #对其他用户所有偏好求和
                sum_R1sq += pow(x, 2) # x的平方和
                sum_R2sq += pow(y, 2) # y的平方和 构建矩阵？
        if n == 0:
            return 0


            # 皮尔逊相关系数计算公式
        den = sqrt(sum_R1sq - pow(sum_R1, 2) / n) * sqrt(sum_R2sq - pow(sum_R2, 2) / n)
        if den == 0:
            return 0
        else:
            return (sum_P - (sum_R1 * sum_R2) / n) / den

    def NearestNeighbor(self, username): # 计算最近邻居
        distances = [] # 定义一个数组
        for instance in self.data:
            if instance != username:
                # print self.data[username]
# self.data[username]是当前用户学习过的课程及评分字典，data[instance]是其他用户学习过的课程和评分字典
                distance = self.fn(self.data[username], self.data[instance])
                distances.append((instance, distance)) # 生成其他用户与当前用户的相似度数组

        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        # print(distances)
        return distances

        # 推荐算法的主体函数

    def recommend(self, user):
        # 定义一个字典，用来存储推荐的书单和分数
        recommendations = {}
        # 计算出user与所有其他用户的相似度，返回一个list
        nearest = self.NearestNeighbor(user)
        # print (nearest)

        userRatings = self.data[user] # 当前用户的所有评分记录
        # print (userRatings)
        totalDistance = 0.0
        # 得住最近的k个近邻的总距离
        for i in range(self.k):
            totalDistance += nearest[i][1]
        if totalDistance == 0.0:
            totalDistance = 1.0

            # 将与user最相近的k个人中user没有看过的书推荐给user，并且这里又做了一个分数的计算排名
        for i in range(self.k):

            # 最近的k个用户中，第i个人的与user的相似度，转换到[0,1]之间，作为权重
            weight = nearest[i][1] / totalDistance

            # 第i个人的name
            name = nearest[i][0]

            # 第i个用户看过的书和相应的打分
            neighborRatings = self.data[name]

            for artist in neighborRatings:
                if not artist in userRatings: # 对于邻居已经学习过的课程，如果当前用户没有学习过
                    if artist not in recommendations: # 且不在推荐列表中
                        recommendations[artist] = (neighborRatings[artist] * weight) # 则将该课程*权重（相似度）,成为一个字典
                    else:
                        recommendations[artist] = (recommendations[artist] + neighborRatings[artist] * weight)

        recommendations = list(recommendations.items()) # 将字典转化为序列
        recommendations = [(self.ProductID2name(k), v) for (k, v) in recommendations] # 取出ID


        # 做了一个排序
        recommendations.sort(key=lambda artistTuple: artistTuple[1], reverse=True) # 排序
        # print(recommendations[:self.n])

        return recommendations[:self.n], nearest


def adjustrecommend(id):
    bookid_list = []
    r = recommender(users)
    k, nearuser = r.recommend("%s" % id)


    for i in range(len(k)):

        bookid_list.append(k[i][0])

    return bookid_list, nearuser[:15]

courseid, near_list = adjustrecommend("Fang Hao")
print ("course_list:", courseid)
print ("near_list:",near_list)