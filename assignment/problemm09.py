from idlelib.pyshell import extended_linecache_checkcache
from selectors import SelectSelector

menu = {
    "삼각김밥": 1200,
    "바나나 우유": 1700,
    "컵라면": 1500,
    "샌드위치": 2500
}
ord = input()
for item in menu:
    if item == ord:
        price = menu[item]
        print(price)
        break

    else:
     print("해당 메뉴는 판매하지 않습니다")





