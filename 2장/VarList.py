odd = [1, 3, 5, 7, 9]
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

#리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))

#리스트 관련 함수
#append 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)

#sort 정렬(오름차순)
a = [1, 4, 2, 3]
a.sort()
print(a)

#reverse 역순
a.reverse()
print(a)

#index 위치 반환
print(a.index(3))

#insert 요소 삽입
a.insert(0, 5)
print(a)

#remove 요소 제거
a.remove(5)
print(a)

#pop 요소 꺼내기
print(a.pop())
print(a)
print(a.pop(1))
print(a)

#count 요소 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

#extend 리스트 확장
a = [1, 2, 3]
a.extend([4, 5])
print(a)
a += [6, 7]
print(a)