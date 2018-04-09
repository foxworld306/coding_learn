# coding=utf-8


from math import sqrt
import random

# fp = open(r"test.txt", "r")

users = {}

for line in open("testtesttest"):
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
    def __init__(self, data, k=6, metric='pearson', n=10):

        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.courseid2name = {}

        self.metric = metric
        if self.metric == 'pearson':
            self.fn = self.pearson
        if type(data).__name__ == 'dict':
            self.couse_rating = data

    def id2name(self, id):

        if id in self.courseid2name:
            return self.courseid2name[id]
        else:
            return id

            # 定义的计算相似度的公式，用的是皮尔逊相关系数计算方法

    def jaccard(self, user, user2):

        c = [val for val in user if val in user2]
        d = list(set(user).union(set(user2)))

        return float(len(c)) / (len(d))



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
                sum_R2sq += pow(y, 2) # y的平方和
        if n == 0:
            return 0


            # 皮尔逊相关系数计算公式
        den = sqrt(sum_R1sq - pow(sum_R1, 2) / n) * sqrt(sum_R2sq - pow(sum_R2, 2) / n)
        if den == 0:
            return 0
        else:
            return (sum_P - (sum_R1 * sum_R2) / n) / den

    def cos_like(self, rating1, rating2):
        innerProd = 0
        vector_x = 0
        vectoy_y = 0
        for key in rating1:
            if key in rating2:
                x = rating1[key]
                y = rating2[key]
                innerProd += x * y
                vector_x += x ** 2
                vectoy_y += y ** 2
        if sqrt(vector_x) * sqrt(vectoy_y) == 0:
            return 0
        else:
            return innerProd / (sqrt(vector_x) * sqrt(vectoy_y))


    # def jaccard(self, p, q):
    #     c = [a for i in p if v in b]
    #     return float(len(c)) / (len(a) + len(b) - len(b))

    # print cos_like(users['Angelica'], users['Bill'])
    # print pearson(users['Angelica'], users['Bill'])
    # for list in (recommend('Veronica', users)):
    #     print list

    def UserSimilarity(self, currentuser): # 计算最相似用户
        similarity = [] # 定义一个数组
        for users in self.couse_rating:
            if users != currentuser:
# self.data[currentuser]是当前用户学习过的课程及评分，data[users]是其他用户学习过的课程和评分
                similar = self.jaccard(self.couse_rating[currentuser], self.couse_rating[users])
                similarity.append((users, similar)) # 生成其他用户与当前用户的相似度数组
                print similarity
        similarity.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return similarity
        # print(similarity[:5])

        # 推荐算法的主体函数

    def recommendation(self, user):
        # 定义一个字典，用来存储推荐的书单和分数
        recommend_list = {}
        # 计算出当前user与其他用户的相似度，返回一个list
        similar_list = self.UserSimilarity(user)
        userRatings = self.couse_rating[user] # 当前用户的所有评分记录
        sum_similarity = 0.0
        for i in range(self.k):
            sum_similarity += similar_list[i][1] # 最相似的k个用户的总距离
        if sum_similarity == 0.0:
            sum_similarity = 1.0
        totalscore = 0.0
        sim_sum = 0.0
        for i in range(self.k):
            # 最近的k个用户中，第i个人的与user的相似度，转换到[0,1]之间，作为权重
            W = similar_list[i][1] / sum_similarity

            similar_username = similar_list[i][0]
            similar_userrating = self.couse_rating[similar_username] # 第i个用户评分过的课程和相应的打分
            for courses in similar_userrating:
                if not courses in userRatings: # 对于邻居已经学习过的课程，如果当前用户没有学习过
                    if courses not in recommend_list: # 且不在推荐列表中
                        sim_sum += similar_list[i][1]
                        totalscore += similar_userrating[courses] * similar_list[i][1]
                        recommend_list[courses] = (totalscore / sim_sum)
                    else:
                        recommend_list[courses] = (recommend_list[courses] + (totalscore / sim_sum))
            # print recommend_list

                    #     recommend_list[courses] = (similar_userrating[courses] * W) # 则将该课程*权重（相似度）
                    # else:
                    #     recommend_list[courses] = (recommend_list[courses] + similar_userrating[courses] * W) # 求和
        recommend_list = list(recommend_list.items()) # 将字典转化为序列
        recommend_list = [(self.id2name(k), v) for (k, v) in recommend_list] # 取出ID
        recommend_list.sort(key=lambda artistTuple: artistTuple[1], reverse=True) # 排序
        # print recommend_list [:3]
        return recommend_list[:self.n], similar_list



def adjustrecommend(id):
    recommend_courses = []
    r = recommender(users)
    k, similar_list = r.recommendation("%s" % id)


    for i in range(len(k)):

        recommend_courses.append(k[i][0])

    return recommend_courses, similar_list[:6]

courseid, similar_users = adjustrecommend("Fang Hao")

print ("recommend_courses:", courseid)
print ("similar_users:", similar_users)