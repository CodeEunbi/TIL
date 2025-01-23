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

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

# missing_book = [
#     '위대한 개츠비',
#     '데미안',
#     '난중일기',
# ]

# is_possible = True
# for i in missing_book:
#     if i not in list_of_book:
#         print(f'{i} 을/를 보충하여야 합니다.')
#         is_possible = False


# for i in [i for i in missing_book if not in ]
#     print(f'{i} 은/는 보유하고 있지 않습니다.')
#     is_possible = False
        
    # for i in [i for i in rental_list if i not in list_of_book]:
    #  print(f'{i} 은/는 보유하고 있지 않습니다.')


#1.list만들기
#missing_books에 정보가 있어서 플래그를 줄 필요가 없음
missing_books = []
for rental in rental_book:
    if rental not in list_of_book:
        missing_books.append(rental)
        
#2.list  
# missing_books = [for rental in rental_book if rental not in list_of_book]
if len(missing_books) == 0:
    print('모든 도서가 대여 가능한 상태입니다.')
else:
    for book in missing_books:
        print(f'{book}보충 필요')

#다른 방법(메세지 출력)
if not missing_books:
    print('모든 도서가 대여 가능한 상태입니다.')
else:
    for book in missing_books:
        print(f'{book}보충 필요')
        
