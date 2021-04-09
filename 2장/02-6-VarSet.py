s1 = set([1,2,3])
print(s1)
s2 = set("Hello")
print(s2)

#특징 : 중복 없음, 순서 없음

#집합(set)의 특징
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
#교집합
print(s1 & s2)
#합집합
print(s1 | s2)
print(s1.union(s2))
#차집합
print(s1 - s2)
print(s1.difference(s2))

#집합 자료형 관련 함수들
#add 값 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#update 값 여러개 추가
s1 .update([5, 6, 7])
print(s1)

#remove 특정 값 제거
s1.remove(7)
print(s1)