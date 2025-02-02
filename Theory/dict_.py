#key - value 로 데이털르 저장하는 자료 구조
my_dict = {}
jeeho = {
    'fname':'Jeeho',
    'lname': 'Park',
}
#새로운 Key에 Value 할당
#만약 이미 있는 key는 덮어쓰기
jeeho['email'] = 'edujeeho@gmail.com'

print(jeeho['fname'])
print(jeeho['lname'])
print(f'{jeeho["fname"]}{jeeho["lname"]}')

#clear
#모든 key : value를 제거
person = {'name':'Alex', 'age':25}
print(f'person : {person}')
person.clear()
print(f'person:{person}')

person = {'name' : 'Alex', 'age':25}
print(person.get('name'))
print(person.get('age'))
print(person.get('country'))    #None
# print(person['country'])      #KeyError
print(person.get('country', 'Unknown'))   #Unknown

#keys
#모든 key를 가진 객체를 반환
print(person.keys())
for key in person.keys():
    print(key)
    
#values
#모든 value들을 가진 객체를 반환한다
print(person.values())
for value in person.values():
    print(value)
    
#items
#모든 k-v쌍을 가진 객체를 반환한다
print(person.items())   #dict_items{('name', 'Alex'),('age', 25)}
for key, value in person.items():
    print(f'{key}-{value}')
    
    
# pop
#주어진 key에 해당하는 데이터를 제거하고 value를 반환한다
person = {'name' : 'Alex', 'age':25}
print(person.pop('name'))
print(person.get('name'))  #None
print(person)

print(person.pop('country', None)) #KeyError


#setdefault
#해당하는 value를 반환하되 없으면 두번째 인자로 설정한다.
person = {'name' : 'Alex', 'age':25}
print(person.setdefault('country', 'South Korea'))
print(person.get('country'))

#update
# 있는 건 덮어쓰기, 없는 인자는 추가