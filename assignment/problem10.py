words ={
    "사과":"apple",
    "바나나":"banana",
    "학교": "school"
}
score =0
for k in words:
    print(k)
    answer=input()
    if answer in words[k]:
        print("정답입니다")
        score = score+1
    else:
        print("아시워요, 정답은",words[k],"입니다")
print("최종 스코어:",score)


