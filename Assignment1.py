"' list inbuild function'"

amcet = ['ai&ds', 'cse', 'ece', 'eee']
print(amcet)   

amcet.append('mech')
print(amcet)

amcet.extend('civil')
print(amcet)

amcet.insert(4,'it')
print(amcet)

amcet.remove('mech')
print(amcet)

amcet.pop(4)
print(amcet)

a = amcet.copy()
print(a)

print(amcet.index('ai&ds'))

amcet.reverse()
print(amcet)

amcet.sort()
print(amcet)


"'dictionary inbuild function'"

amcet = {"dept":"ai&ds","strength":26, "batch":2025}
print(amcet)

amcet.clear()

x = amcet.copy()
print(x)

x = {"cse":68,"ece":48,"eee":30}
amcet = amcet.fromkeys(x)
print(amcet)

x = amcet.get("dept")
print(x)

x = amcet.items()
print(x)

x = amcet.keys()
print(x)

x = amcet.setdefault("strength", 65)
print(x)

amcet.update({"rep": 2})
print(amcet)

x = amcet.values()
print(x)

amcet.popitem()
print(amcet)


"'tuples inbuild function'"


amcet = ('ai&ds','cse','ece','eee','mech','civil','it')

x = amcet.count(4)
print(x)

x = amcet.index('it')
print(x)




"""
['ai&ds', 'cse', 'ece', 'eee']
['ai&ds', 'cse', 'ece', 'eee', 'mech']
['ai&ds', 'cse', 'ece', 'eee', 'mech', 'c', 'i', 'v', 'i', 'l']
['ai&ds', 'cse', 'ece', 'eee', 'it', 'mech', 'c', 'i', 'v', 'i', 'l']
['ai&ds', 'cse', 'ece', 'eee', 'it', 'c', 'i', 'v', 'i', 'l']
['ai&ds', 'cse', 'ece', 'eee', 'c', 'i', 'v', 'i', 'l']
['ai&ds', 'cse', 'ece', 'eee', 'c', 'i', 'v', 'i', 'l']
0
['l', 'i', 'v', 'i', 'c', 'eee', 'ece', 'cse', 'ai&ds']
['ai&ds', 'c', 'cse', 'ece', 'eee', 'i', 'i', 'l', 'v']
{'dept': 'ai&ds', 'strength': 26, 'batch': 2025}
{}
{'cse': None, 'ece': None, 'eee': None}
None
dict_items([('cse', None), ('ece', None), ('eee', None)])
dict_keys(['cse', 'ece', 'eee'])
65
{'cse': None, 'ece': None, 'eee': None, 'strength': 65, 'rep': 2}
dict_values([None, None, None, 65, 2])
{'cse': None, 'ece': None, 'eee': None, 'strength': 65}
0
6
"""
