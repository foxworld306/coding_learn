# format = 'Hello %s. %s enough for ya?' # %s是转换说明符，标记了需要插入转换值的位置。s表示值会被格式化为字符串
# value = ('world', 'hot')
# print(format % value)

# from math import pi
# format = 'Pi with three decimals: %.3f' # %f 格式化浮点数，.3表示精度
# print(format % pi)

# # 模板字符串
# from string import Template
# s = Template('$x, come on $x!')
# print(s.substitute(x = 'AB'))
#
# from string import Template
# s = Template('A $someone must never $action')
# d = {} # 使用字典变量提供值/名称对
# d['someone'] = 'gentleman'
# d['action'] = 'show his socks'
# print(s.safe_substitute(d)) #使用safe_substitute不会因为缺少值或者不正确使用$字符出错

# s = '{},{} and {}'.format('1', '2', '3')
# print(s)

# from math import pi
# print('-%10.2f'% pi) # 字段宽度为10，空格填充，如果在10前加0，则为0填充,-为左对齐
# print(('%+5d'% 10) + '\n' + ('%+5d' % -10)) # +表示不管正数负数都标示出符号

# # 3-1 coding example
#
# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width
# header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
# fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
# print('=' * width)
# print(header_fmt.format('Item', 'Price'))
# print('-' * width)
# print(fmt.format('Apples', 0.4))
# print(fmt.format('Pears', 0.5))
# print(fmt.format('Cantaloupes', 1.92))
# print(fmt.format('Dried Apricots (16 oz.)', 8))
# print(fmt.format('Prunes (4 lbs.)', 12))
# print('=' * width)

# # find方法，返回数值，不是布尔值
# s = 'AB come on come on go to school'
# print(s.find('c'))

# # join方法,把+加入到s序列中去
# s = ['ab','come','on']
# p = '+'
# print(p.join(s))

# #replace方法
# print('this is a test'.replace('is', 'at'))
#
# # split方法
# s = 'ab-come-on'
# print(s.split('-'))