from pprint import pprint
d = dict()

d['a'] = 1
d['b'] = 5
d['c'] = 7

pprint(d,width=1)

d = {
    'a' : 1,
    'b' : 5,
    'c' : 7
}

pprint(d,width=1)

print(d['a'])
#print(d['z'])#ERROR
if 'z' in d:
    print(d['z'])
else:
    print('No existe la llave')
