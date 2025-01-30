#함수 2개 사용
def rental_book(name, number):
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(number):
    print(f'남은 책의 수 : {number_of_book - number} ')

result = decrease_book(3), rental_book('홍길동', 3)

#함수 1개 사용
def rental_book(name, number):
    print(f'남은 책의 수 : {number_of_book - number}')
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

result = rental_book('홍길동', 3)