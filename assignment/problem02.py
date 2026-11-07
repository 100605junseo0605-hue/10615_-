num = int(input("첫 번째 숫자를 입력하시오"))
num2 = int(input("두 번째 숫자를 입력하십시오"))
cal = input("연산자")

if cal == "+":
    print(num + num2)

elif cal == "-":
    print(num - num2)

elif cal == "*":
    print(num * num2)

elif cal == "/":
    print(num / num2)

else:
    print("잘못 된 연산자 입니다.")
