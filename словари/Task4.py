a = {
    'Conor': 'habib',
    'leonardo': 'brassic',
    'Jon': 'gay',
    'Woody': 'wood',
    'OGBUDA': 'singer'
}
b = a['OGBUDA']
a['singer'] = a['OGBUDA']
a['singer'] = b
a.pop('leonardo')
a.update({'new_key': 'new_value'})
print(a)
