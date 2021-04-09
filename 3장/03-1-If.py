#돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#주의할 것 : 들여쓰기, 콜론

#비교연산자 : >, <, ==, !=, >=, <=
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#논리연산자 : and, or , not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#in 연산자 : x in s, x not in s
pocket = ['paper', 'cellphone', 'money']
if money in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#pass : 아무일도 하지 않게
if money in pocket:
    pass
else:
    print("걸어 가라")
