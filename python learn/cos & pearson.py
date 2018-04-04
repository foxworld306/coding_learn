# -*- coding:utf8 -*-
from math import sqrt
#
# users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
#                       "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
#          "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
#                   "Vampire Weekend": 3.0},
#          "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
#                   "Slightly Stoopid": 1.0},
#          "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
#                  "The Strokes": 4.0, "Vampire Weekend": 2.0},
#          "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
#                     "Vampire Weekend": 1.0},
#          "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
#                     "The Strokes": 4.0, "Vampire Weekend": 4.0},
#          "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
#                  "Slightly Stoopid": 4.0, "The Strokes": 5.0},
#          "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
#                       "The Strokes": 3.0}
#          }


users = {"user1": {"item101": 5.0, "item102": 3.0, "item103": 2.5},
"user2": {"item101": 2.0, "item102": 2.5, "item103": 5.0},
"user3": {"item101": 2.5},
"user4": {"item101": 5.0,"item103": 3.0},
"user5": {"item101": 4.0, "item102": 3.0, "item103": 2.0}
         }
#                       "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
#          "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
#                   "Vampire Weekend": 3.0},

def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1  # Indicates no ratings in common


# 欧几里距离
def euclidean(rating1, rating2):
    """Computes the Euclidean distance. Both rating1 and rating2 are dictionaries
        of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            # distance += sqrt((rating1[key]-rating2[key])**2)
            distance += (rating1[key] - rating2[key]) ** 2
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1

    # 明氏距离


def minkowski(rating1, rating2, r):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key] - rating2[key]), r)
            commonRatings = True
            return pow(distance, 1 / r)
        else:
            return -1


def computeNearestNeighbor(username, users):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            distance = sim_distance_jaccard(users[user], users[username])
            distances.append((distance, user))
            # sort based on distance -- closest first
    distances.sort(reverse=True)
    print(distances)
    return distances


def recommend(username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, users)[0][1]
    print nearest

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
            # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)


# examples - urncomment to run


# print( recommend('Hailey', users))
def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += x ** 2
            sum_y2 += y ** 2
    denominnator = sqrt(sum_x2 - (sum_x ** 2) / n) * sqrt(sum_y2 - (sum_y ** 2) / n)
    if denominnator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominnator


def cos_like(rating1, rating2):
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

def sim_distance_jaccard(p1,p2):
    c = set(p1.keys())&set(p2.keys())
    if not c:
        return 0
    ss = sum([p1.get(sk)*p2.get(sk) for sk in c])
    sq1 = sum([pow(sk,2) for sk in p1.values()])
    sq2 = sum([pow(sk,2) for sk in p2.values()])
    p = float(ss)/(sq1+sq2-ss)
    return p


# print cos_like(users['Angelica'], users['Bill'])
# print pearson(users['Angelica'], users['Bill'])
for list in (recommend('user1', users)):
    print list