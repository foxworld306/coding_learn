# url = input('enter your url:')
# print('domain name is ' + url[11:-4])
#
# # 步长显示, 步长为2
# n = [1,2,3,4,5,6,7,8,9,10]
# print(n[0:10:2])
# print(n[3:6:3])
# print(n[::4])
# print(n[8:3:-2])
#
#
# # 2-3 Prints a sentence in a centered "box" of correct width
#
# sentence = input("Sentence: ")
#
# screen_width = 80
# text_width   = len(sentence)
# box_width    = text_width + 6
# left_margin  = (screen_width - box_width) // 2
#
# print()
# print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
# print(' ' * left_margin + '|  ' + ' ' * text_width     + '  |')
# print(' ' * left_margin + '|  ' +       sentence       + '  |')
# print(' ' * left_margin + '|  ' + ' ' * text_width     + '  |')
# print(' ' * left_margin + '+'   + '-' * (box_width-2)  +   '+')
# print()
#
# # check if an item in a list
# n = 'come'
# print('c' in n)
# print('n' in n)
# x = ['tempo', 'nescafe', 'coca']
# # s = input('enter your name: ')
# print (input('enter your name:') in x)
#
# database = [
#     ['albert',  '1234'],
#     ['dilbert', '4242'],
#     ['smith',   '7524'],
#     ['jones',   '9843']
# ]
# username = input('enter your name: ')
# pin = input('enter your pin: ')
# if [username, pin] in database:
#     print('grant access')
# else:
#     print('access denied')

# L = [78, 89, 1, 23]
# print(len(L))
# print(max(L))
# print(min(L))
# print(max(7,1,8))
# del L[2]
# print(L)

# #分片
# name = list('Nescafe')
# print(name)
# name[2:] = list('par')
# print(name)

# #方法：对象.方法（参数）
# L = list('1234567890')
# L.append('0')
# print(L)
# print(L.count('0'))
#
# P = list('456')
# L.extend(P)
# print(L)
#
# print(L.index('4'))
# L.insert(2, '2')
# print(L)
# print(L.pop(0))
# L.remove('2')
# print(L)
# L.reverse() #反向存放
# print(L)
#
# x = list('321')
# # y = x[:] #必须要有[:],实现赋值
# y = sorted(x)
# # y.reverse()
# print(y)
# print(x)
# L.sort()  #排序
# print(L)

#比较
L = list('123')
Q = reversed(L)
print(Q)
