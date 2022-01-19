# 1번 문제
score = {"국어": 95, "영어": 90, "수학": 80, "과학": 50 }
average = sum(score.values()) / len(score)

#2번 문제
mul_3 = {i for i in range(100) if i % 3 == 0}
mul_5 = {i for i in range(100) if i % 5 == 0}
result_2_1 = mul_3 & mul_5  #3과 5의 공배수 
result_2_2 = mul_3 | mul_5  #합집합

#3번 문제
result_3 = list(range(7, -8, -2))

#4번 문제 
result_4 = tuple(result_3)


temp = 0
