# coding=utf-8
from math import *


movie_list = {} #id:title
with open("d:/u.item") as f:
    for line in f.readlines():
        (mid, title) = line.split('|')[0:2]
        movie_list[mid] = title
pref_by_people = {}
with open("d:/u.data") as f:
    for line in f.readlines():
        (uid, mid, rating) = line.split('\t')[0:3]
        if not uid in pref_by_people.keys():
            pref_by_people[uid] = {}
        pref_by_people[uid][movie_list[mid]] = int(rating)

def TransfromPref(pref):
    re_pref = {}
    for k1, v1 in pref.items():
        for k2, v2 in v1.items():
            if not k2 in re_pref.keys():
                re_pref[k2] = {}
            re_pref[k2][k1] = v2
    return re_pref

pref_by_movie = TransfromPref(pref_by_people)

def Pearson(pref , movie1, movie2):
#找出对两部电影都评论的人
    people_list = [person for person in pref[movie1].keys() if person in pref[movie2].keys()]
    n = len(people_list)
    if n == 0:
        return 0
    #计算评价和
    sum1 = sum([pref[movie1][person] for person in people_list])
    sum2 = sum([pref[movie2][person] for person in people_list])
    #计算评价平方和
    sumSq1 = sum([pref[movie1][person] ** 2 for person in people_list])
    sumSq2 = sum([pref[movie2][person] ** 2 for person in people_list])
    #计算评价成绩和
    psum = sum([pref[movie1][person] * pref[movie2][person] for person in people_list])
    # 皮尔逊相关系数计算
    num = psum - sum1 * sum2 / n
    den = sqrt((sumSq1 - (sum1 ** 2) / n) * (sumSq2 - (sum2 ** 2) / n))

    if den == 0:
        return 0
    return num / den

def TopMatch(pref, movie, n = 5):
    #计算给电影和每部电影的皮尔逊相关系数
    scores = [(Pearson(pref_by_movie, movie, mov), mov) for mov in pref_by_movie.keys() if mov != movie]
    #根据系数进行排序，并由大到小排序
    scores.sort(key = lambda x:x[0], reverse = True)
    return scores[0:n]

def CreateMatchList(pref = pref_by_movie):
    match_list = {}
    for movie in pref.keys():
        match_list[movie] = TopMatch(pref, movie, 5)
    return match_list

match_list = CreateMatchList()

def get_recommanded_items(pref = pref_by_people, match_list = match_list, user = '1'):
    try:
        user_ratings = pref[user] #找出用户看过的电影与评价
    except KeyError:
        print("no user")
        return 0
    scores = {} #记录加权和
    totalsim = {} #记录评分和

    for movie, rating in user_ratings.items(): #遍历当前用户评分电影
        for sim, sim_movie in match_list[movie]: #遍历当前电影相近电影
            if sim_movie in user_ratings.keys(): #如果用户看过该电影，跳出本次循环
                continue
             #记录加权和与评分和
            if not sim_movie in scores.keys():
                scores[sim_movie] = sim * rating
                totalsim[sim_movie] = sim
            scores[sim_movie] += sim * rating
            totalsim[sim_movie] += sim

    rankings = [(scores[sim_movie]/totalsim[sim_movie], sim_movie) for sim_movie in scores.keys() if totalsim[sim_movie] != 0]
    #排序并取前5
    rankings.sort(key=lambda x:x[0], reverse=True)
    print rankings [:5]
    return rankings[0:5]
