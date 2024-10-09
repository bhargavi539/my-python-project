# Ordered List
# It remembers the order of the insertion of elements

from collections import OrderedDict,defaultdict

# dic = {'name':'Amritha','age':'35','phone':'6272829','address':'NYC 2560'}
# print(dic)

d = dict()
d['name'] = 'Amrita'
d['age'] = '35'
d['phone'] = '6272829'
d['address'] = 'NYC 2560'

od = OrderedDict()
od['StudentsinPythoncourse'] = 230
od['StudentsinJavacourse'] = 199
od['StudentsinGitcourse'] = 52
print(od)

dd = defaultdict(int)
dd['1'] = 'Ameer'
dd['2'] = '235326'
print(dd)
print(dd['d'])