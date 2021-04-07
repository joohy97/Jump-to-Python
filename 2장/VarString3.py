#문자열 관련 함수
#count 개수 세기
a = "hobby"
print(a.count('b'))

#find 위치 알려주기
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

#index 위치 알려주기
a = "Life is too short"
print(a.index('t'))
#print(a.index'k')) #오류

#join 문자열 사이에 삽입
print(",".join('abcd'))

#upper 대문자로
a = "hi"
print(a.upper())

#lower 소문자로
a = "HI"
print(a.lower())

#lstrip 왼쪽 공백 제거
a = " hi "
print(a.lstrip())

#rstrip 오른쪽 공백 제거
print(a.rstrip())

#strip 양쪽 공백 제거
print(a.strip())

#replace 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#split 문자열 나누기
print(a.split())
b = "a:b:c:d"
print(b.split(':'))