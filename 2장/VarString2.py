#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3]) #0부터 숫자 세므로 4번째인 e 출력

#문자열 인덱싱 활용
print(a[0])
print(a[12])
print(a[-1]) #마지막 문자

#문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])
print(a[5:7])
print(a[12:17])

#슬라이싱으로 문자열 나누기
c = "20210407Sunny"
date = c[:8]
weather = c[8:]
print(date, weather)

#문자열 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
print("I ate %d apples. So I was sick for %s days." % (10, "three"))

#f문자열 포매팅
name = '홍길동'
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
print(f"나는 내년이면 {age + 1}살이 된다")