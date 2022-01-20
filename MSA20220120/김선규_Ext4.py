score_1 = [95, 90, 80 , 50]
score_2 = [100, 50, 90, 90]
score_3 = [99, 60, 100, 40]
score_4 = [55, 80, 80, 60]

#각자합
sum_1 = 0
i = 0

while True:
    if i == len(score_1):
        break
    elif i < len(score_1):
        sum_1 += score_1[i]
        i += 1

sum_2 = 0
i = 0

while True:
    if i == len(score_2):
        break
    elif i < len(score_2):
        sum_2 += score_2[i]
        i += 1

sum_3 = 0
i = 0

while True:
    if i == len(score_3):
        break
    elif i < len(score_3):
        sum_3 += score_3[i]
        i += 1

sum_4 = 0
i = 0

while True:
    if i == len(score_4):
        break
    elif i < len(score_4):
        sum_4 += score_4[i]
        i += 1

#각자 평균
avg_1 = sum_1 / len(score_1)
avg_2 = sum_2 / len(score_2)
avg_3 = sum_3 / len(score_3)
avg_4 = sum_4 / len(score_4)

#전체합
total_sum = sum_1 + sum_2 + sum_3 + sum_4

#전체 평균
total_avg = total_sum / 4
    
temp = 0
    




