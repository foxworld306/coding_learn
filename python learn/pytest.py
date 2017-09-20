import random

fp = open(r"test.txt", "r")

users = {}

for line in open("test.txt"):
    lines = line.strip().split(",")
    lines[2] = random.uniform(1,5)
    if lines[0] not in users:
        users[lines[0]] = {}
        # print(users)
    users[lines[0]][lines[2]] = (lines[1])
    print (users)


# print(users)



    # print(users)