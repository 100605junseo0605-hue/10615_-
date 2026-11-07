password = "python123"
while 1:
    tipe = input()
    if tipe == password:
        print("로그인 성공!")
        break
else:
    print("비밀번호가 틀렸습니다. 다시 입력하세요")