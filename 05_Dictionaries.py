my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key2'])  # value2
my_dict = {'key1': 123, 'key2': [12, 23, 33], 'key3': ['item0', 'item1', 'item2']}  # Different Data Types
print(my_dict['key3'])  # ['item0', 'item1', 'item2']
print(my_dict['key3'][0])  # item0
print(my_dict['key3'][0].upper())  # ITEM0
my_dict['key1'] = my_dict['key1'] - 122  # OR my_dict['key1'] -= 122
print(my_dict['key1'])  # Prints 1

# Create A New Dictionary
d = {}
d['person'] = 'Alex'
d['money'] = 0.00
print(d)  # {'person': 'Alex', 'money': 0.0}

# Nesting with Dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])  # Prints value

# A few Dictionary Methods
d = {'key1':1,'key2':2,'key3':3}
print(d.keys())  # Prints dict_keys(['key1', 'key2', 'key3'])
print(d.values())  # Prints dict_values([1, 2, 3])
print(d.items())  # Prints dict_items([('key1', 1), ('key2', 2), ('key3', 3)])
