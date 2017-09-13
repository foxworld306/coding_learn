# _*_ encoding:utf-8 _*_


# # 字典用{},字典中的key是唯一的，value不唯一
# phonebook = {'ab':'0123', 'zd':'1234', 'ev':'2345'}
# print(phonebook['ab'])

# # dict函数
# s = dict(name='zd', age='40')
# print(s)
# print(len(s))
# print(s['name'])
# s['name'] = 'pc'
# print(s)
# p = {}
# p['country'] = 'china' #将china赋值给country
# print(p)

# people  ={
#     'Alice': {
#         'Phone':'8484',
#         'Addr': 'gogo street 123'
#     },
#     'Beth':{
#         'Phone': '3848',
#         'Addr': 'comco 1324'
#     },
#     'Ceser':{
#         'Phone':'1234',
#         'Addr':'dosscom 23'
#     }
# }
#
# labels = {
#     'Phone':'phone number',
#     'Addr': 'Address'
# }
# name = input('your name is: ')
# request = input('Phone number (p) or address (a)? ')
#
# # Use the correct key:
# if request == 'p': key = 'Phone'
# if request == 'a': key = 'Addr'
#
# # Only try to print information if the name is a valid key in
# # our dictionary:
# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
scores=[("zhang",100),("wang",98),("li",78)]
print(scores[0])
print(scores[0][0])