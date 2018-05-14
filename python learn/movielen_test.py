# -*- coding: utf-8 -*-
__author__ = 'ustc'

import random
import math

M = 8  # 数据集随机分成M份
N = 10  # top-N
K = 80  # 与用户相近的K个用户
k = 2
seed = 7  # 随机数种子


# 获取数据
def GetData():
    f = open('D:/ratings.dat', 'r')
    # f = open('D:\\text.txt', 'r')
    originalData = f.readlines()  # 原始数据
    f.close()
    data = []  # 处理后的数据
    # for循环中为处理原始数据的过程，处理后的形式为[user,item]
    for infoStr in originalData:
        infoList = infoStr.split('::')
        user = infoList[0]
        item = infoList[1]
        data.append([user, item])
    return data


def SpitData(data, M, k, seed):  # data原始数据集，M份数，0<=k<=M-1,seed随机数种子，不变
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test


def UserSimilarity(train):
    # 先构造物品到用户的倒排表
    item_users = dict()
    for u, items in train:
        for i in items:
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    # 计算用户间的相关系数
    C = dict()
    N = dict()  # N[u]表示用户u曾经有过的正反馈物品个数
    for i, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 1
            else:
                N[u] += 1
            C[u] = dict()
            for v in users:
                if u == v:
                    continue
                if v in C[u]:
                    C[u][v] += 1
                else:
                    C[u][v] = 1


    for u, related_users in C.items():
        W[u] = dict()
    for v, cuv in related_users.items():
        W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W


# 改进的相似度计算方法
def UserSimilarity_IIF(train):
    # 先构造物品到用户的倒排表
    item_users = dict()
    for u, items in train:
        for i in items:
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    # 计算用户间的相关系数
    C = dict()
    N = dict()  # N[u]表示用户u曾经有过的正反馈物品个数
    for i, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 1
            else:
                N[u] += 1
            C[u] = dict()  # C的结构是{
            for v in users:
                if u == v:
                    continue
                if v in C[u]:
                    C[u][v] += 1 / math.log(1 + len(users))
                else:
                    C[u][v] = 1

        for u, related_users in C.items():
            W[u] = dict()
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
        return W


#
def Recommend(user, train, W):
    rank = dict()  # rank存放的是对未参与过的物品i的兴趣度
    interacted_items = []  # 获取训练数据中用户user参与正反馈的物品
    for u in train:
        if user == u[0]:
            interacted_items.append(u[1])
    for v, wuv in sorted(W[user].items(), key=lambda x: x[1], reverse=True)[0:K]:
        trainv = []
        for tr in train:
            if tr[0] == v:
                trainv.append(tr[1])
        for i in trainv:
            if i in interacted_items:
                continue  # 除去用户user曾参与过的物品
            if i not in rank:
                rank[i] = wuv * 1.0  # 1.0可以理解为用户对物品的兴趣度，因为本例忽略了对物品的评分记录，使用的是单一行为的隐反馈数据
            else:
                rank[i] += wuv * 1.0
    return rank


# 获取最终的推荐列表 top-N
def GetRecommendation(userRank, N):
    rank = []
    for item, value in sorted(userRank.items(), key=lambda x: x[1], reverse=True)[0:N]:
        rank.append([item, value])
    return rank


# 计算准确率
def Precision(train, test, user, userRank, N):
    hit = 0
    all = 0
    tu = []
    for te in test:
        if te[0] == user:
            tu.append(te[1])
    for item, value in userRank:
        if item in tu:
            hit += 1
    all += N
    return hit / (all * 1.0)


# 计算召回率
def Recall(train, test, user, userRank):
    hit = 0
    all = 0
    tu = []
    for te in test:
        if te[0] == user:
            tu.append(te[1])
    for item, value in userRank:
        if item in tu:
            hit += 1
    all += len(tu)
    return hit / (all * 1.0)


if __name__ == '__main__':
    user = '7'
    data = GetData()
    train, test = SpitData(data, M, k, seed)
    W = UserSimilarity(train)
    ranktemp = dict()
    ranktemp = Recommend(user, train, W)
    rank = GetRecommendation(ranktemp, N)
    recall = Recall(train, test, user, rank)
    precision = Precision(train, test, user, rank, N)
    print 'recall=%f' % recall
    print 'precision=%f' % precision