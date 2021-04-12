# Q6
f = open("4장/test1.txt", "a")
while True:
    a = input("작성할 내용을 입력하세요 : ")
    if a == "":
        break
    else:
        f.write(a + '\n')

f.close()