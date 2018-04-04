#-*-coding:utf-8 -*-
# 计算jaccard系数


users = {"user1": {"item101": 5.0, "item102": 3.0, "item103": 2.5},
"user2": {"item101": 2.0, "item102": 2.5, "item103": 5.0},
"user3": {"item101": 2.5},
"user4": {"item101": 5.0,"item103": 3.0},
"user5": {"item101": 4.0, "item102": 3.0, "item103": 2.0}
         }


# p = ['shirt','shoes','pants','socks']
# q = ['shirt','shoes']

p = ['1','2','3','4']
q = ['3','4','5','6']


def jaccard(p,q):

    c = [val for val in p if val in q]
    d = list(set(p).union(set(q)))

    return float(len(c))/(len(d))
print jaccard(p,q)


a=[2,3,4,5]
b=[2,5,8]
tmp = [val for val in a if val in b]
print tmp