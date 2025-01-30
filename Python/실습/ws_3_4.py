def create_user(name, age, address):
    user_info = {
        'name': name,
        'age': age,
        'address': address,
    }
    
    for n in name:
        print(f"{n}님 환영합니다!")
    
    users = [
        {'name': user_info['name'][i], 'age': user_info['age'][i], 'address': user_info['address'][i]} 
        for i in range(len(name))
    ]
    
    return users

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

result = create_user(name, age, address)
print(result)


# zip()을 사용하면 좀 더 편리하게 할 수 있을 것 같음