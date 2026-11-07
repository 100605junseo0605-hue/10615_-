age = int(input("나이를 입력 하세요"))
print(age)

if age < 8:
    print("입장료는 0원 입니다.")

elif age <= 19:
    print("입장료는 10,000원 입니다.")

elif age <= 64:
    print("입장료는 20,000원 입니다.")

else:
    print("입장료는 5000원 입니다.")

