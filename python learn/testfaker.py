# coding=utf-8

from faker import Faker
import random
from random import randint


fake = Faker('zh_CN')

    # print fake.pyfloat(left_digits=1, right_digits=0, positive=True)
    # print fake.pydecimal(left_digits=1, right_digits=0, positive=True)
# print fake.profile(fields='username')
for x  in range(0, 375):
    print fake.romanized_name()
#     print fake.building_number()

