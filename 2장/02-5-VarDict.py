#{Key1:Value1, Key2:Value2, Key3:Value3, ...}

dic = {'name':'pey', 'phone':'01133334444', 'birth':'1118'}

#딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)

#딕셔너리 요소 삭제하기
del a[1]
print(a)

#딕셔너리 관련 함수들
#keys 키 리스트 만들기
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

#values 밸류 리스트 만들기
print(a.values())

#items 키, 밸류 쌍 얻기
print(a.items())

#clear 쌍 모두 지우기
print(a.clear())

#get 키로 밸류 얻기
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a['name'])

#in 해당 키가 있는 지 조사
print('name' in a)
print('email' in a)