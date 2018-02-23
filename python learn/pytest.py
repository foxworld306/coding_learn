import random


# fp = open(r"test.txt", "r")
#
# users = {}
#
# for line in open("test.txt"):
#     lines = line.strip().split(",")
#     lines[2] = random.uniform(1,5)
#     if lines[0] not in users:
#         users[lines[0]] = {}
#         # print(users)
#     users[lines[0]][lines[2]] = (lines[1])
#
#     print (users)

# print(users)



    # print(users)

import random

x = [random.randint(1, 413) for _ in range(5310)]
# [57, 93, 22, 55, 41, 64, 47, 32, 93, 61]
print x