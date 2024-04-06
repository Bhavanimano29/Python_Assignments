dict={
    'dict_1':{'clg':'amcet','dept':'ai&ds','strength':26},
    'dict_2':{'clg':'global','dept':'cse','strength':60},
    'dict_3':{'clg':'kingston','dept':'IT','strength':65},
    'dict_4':{'clg':'hakeem','dept':'ece','strength':40}
}

print("nested dictionary")
print(dict)

dict['dict_5']={'clg':'srm','dept':'eee','strength':50}
print("\n adding element to dictionary")
print(dict)

print("\n accessing element")
print(dict['dict_1']['clg'])
print(dict['dict_4']['strength'])

print("\n deleting element")
del dict['dict_2']
print(dict)



my_set1 = {'bhuvi','uma','ezhil','sneaha','divi','rahila','preethi'}
my_set2 = {'preethi','rahila','ramya','sumithra','keerthi','shabana'}

my_set1.add('sarala')
print("After adding 'sarala':", my_set1)

my_set2.remove('ramya')
print("After removing 'ramya':", my_set2)

print("Length of the set:", len(my_set1))

print("Is 'bhuvi' present in the set?", 'bhuvi' in my_set1)

union_set = my_set1.union(my_set2)
print("Union of sets:", union_set)

intersection_set = my_set1.intersection(my_set2)
print("Intersection of sets:", intersection_set)

difference_set = my_set1.difference(my_set2)
print("Difference of sets (set1 - set2):", difference_set)

symmetric_difference_set = my_set1.symmetric_difference(my_set2)
print("Symmetric difference of sets:", symmetric_difference_set)

subset = {'uma', 'ezhil'}
print("Is {'uma', 'ezhil'} a subset of {'bhuvi','uma','ezhil','sneaha','divi','rahila','preethi'}?", subset.issubset(my_set1))
print("Is {'bhuvi','uma','ezhil','sneaha','divi','rahila','preethi'} a superset of {'uma', 'ezhil'}?", my_set1.issuperset(subset))

subset.clear()
print("Cleared set:", subset)




a=int(input("A"))
b=int(input("B"))

operation=input("add/sub/multi/div:")

if(operation=="add"):
 print(a+b)

elif(operation=="sub"):
 print(a-b)

elif(operation=="multi"):
 print(a*b)

elif(operation=="div"):
 print(a/b)

else:
  print("invalid")

count=0

for i in range(1,190):
  if(i%3==0 and i%5==0):
    count=count+1
print(count)  
  
  
  
  
"""
 nested dictionary
 {'dict_1': {'clg': 'amcet', 'dept': 'ai&ds', 'strength': 26}, 'dict_2': {'clg': 'global', 'dept': 'cse', 'strength': 60}, 'dict_3': {'clg': 'kingston', 'dept': 'IT', 'strength': 65}, 'dict_4': {'clg': 'hakeem', 'dept': 'ece', 'strength': 40}}

 adding element to dictionary
 
 {'dict_1': {'clg': 'amcet', 'dept': 'ai&ds', 'strength': 26}, 'dict_2': {'clg': 'global', 'dept': 'cse', 'strength': 60}, 'dict_3': {'clg': 'kingston', 'dept': 'IT', 'strength': 65}, 'dict_4': {'clg': 'hakeem', 'dept': 'ece', 'strength': 40}, 'dict_5': {'clg': 'srm', 'dept': 'eee', 'strength': 50}}

 accessing element
 
 amcet
 40

 deleting element
 
 {'dict_1': {'clg': 'amcet', 'dept': 'ai&ds', 'strength': 26}, 'dict_3': {'clg': 'kingston', 'dept': 'IT', 'strength': 65}, 'dict_4': {'clg': 'hakeem', 'dept': 'ece', 'strength': 40}, 'dict_5': {'clg': 'srm', 'dept': 'eee', 'strength': 50}}
 set after adding
 {'sneaha', 'uma', 'divi', 'preethi', 'sarala', 'bhuvi', 'ezhil', 'rahila'}

 After adding 'sarala': {'uma', 'ezhil', 'sarala', 'divi', 'sneaha', 'bhuvi', 'preethi', 'rahila'}
 After removing 'ramya': {'sumithra', 'keerthi', 'shabana', 'preethi', 'rahila'}
 Length of the set: 8
 Is 'bhuvi' present in the set? True
 Union of sets: {'sumithra', 'uma', 'ezhil', 'sarala', 'divi', 'shabana', 'bhuvi', 'preethi', 'rahila', 'sneaha', 'keerthi'}
 Intersection of sets: {'preethi', 'rahila'}
 Difference of sets (set1 - set2): {'uma', 'ezhil', 'sarala', 'divi', 'bhuvi', 'sneaha'}
 Symmetric difference of sets: {'sumithra', 'ezhil', 'divi', 'shabana', 'sneaha', 'uma', 'sarala', 'bhuvi', 'keerthi'}
 Is {'uma', 'ezhil'} a subset of {'bhuvi','uma','ezhil','sneaha','divi','rahila','preethi'}? True
 Is {'bhuvi','uma','ezhil','sneaha','divi','rahila','preethi'} a superset of {'uma', 'ezhil'}? True
 Cleared set: set()

 A15
 B25
 add/sub/multi/div:multi
 375
 12
 """