dic = {
    'name':['alex','wusir','taibai'],
    'py9':{
        'time':'1213',
        'learn_money':19800,
        'addr':'CBD',
           },
    'age':21
}
# dic['age'] = 56
# print(dic['name'])
# dic['name'].append('ritian')
# l = [1,2,'wusir']
# l[2] = l[2].upper()
# dic['name'][1] = dic['name'][1].upper()
# print(dic)

# female : 6
# dic['py9']['female'] = 6
# print(dic)

#  找出字符串中的数字，并计算个数:fhdklah123rfdj12fdjsl3    '       123     12    13'
info = input(">>>")
for i in info:
    if i.isalpha():
        info = info.replace(i, " ")
l1 = info.split()
print(l1, len(l1))