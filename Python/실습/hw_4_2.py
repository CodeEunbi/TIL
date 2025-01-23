list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

# looking_for = '옥련몽'
found = False 

# for owned in list_of_book:
#     if owned == looking_for:
#         # print('있다!')
#         found = True

# if found:
#     print('있다!')
# else:
#     print('없다..')
    
    
rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

#나
is_possible = True
for i in rental_list:
    if i not in list_of_book:
        print(f'{i} 은/는 보유하고 있지 않습니다.')
        is_possible = False
        break

if is_possible:
    print('모든 도서가 대여 가능합니다.')
    
# print(is_possible)    
#  for i in [i for i in rental_list if i not in list_of_book]:
#      print(f'{i} 은/는 보유하고 있지 않습니다.')

#강사님
#책찾기
# good_to_go = True
# for rental in rental_list:
#     found = False
#     for book in list_of_book:
#         if book == rental:
#             found = True
#             break
# #     #책이 없으면
# #     if not found :
# #         print(f'{rental} 은/는 보유하고 있지 않습니다.')
# #         good_to_go = False
# #  #책이 있으면
# # if good_to_go:
# #     print('모든 도서가 대여 가능한 상태입니다.')
    
    
    
# if rental not in list_of_book:
#     print(f'{rental} 은/는 보유하고 있지 않습니다.')
#     good_to_go = False
    
# if good_to_go:
#     print('모든 도서가 대여 가능한 상태입니다.')

