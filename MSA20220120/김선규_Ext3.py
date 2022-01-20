score_1 = [95, 90, 80 , 50]
score_2 = [100, 50, 90, 90]
score_3 = [99, 60, 100, 40]
score_4 = [55, 80, 80, 60]

#각자 합
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0

n = 0
i = 0

while n < len(score_1):
    sum_1 = sum_1 + score_1[n]
    n = n + 1

n = 0
i = 0

while n < len(score_2):
    sum_2 = sum_2 + score_2[n]
    n = n + 1

n = 0
i = 0

while n < len(score_3):
    sum_3 = sum_3 + score_3[n]
    n = n + 1

n = 0
i = 0

while n < len(score_4):
    sum_4 = sum_4 + score_4[n]
    n = n + 1

#각자 평균
avg_1 = sum_1 / 4
avg_2 = sum_2 / 4
avg_3 = sum_3 / 4
avg_4 = sum_4 / 4

#전체합
total_sum = sum_1 + sum_2 + sum_3 + sum_4

#전체 평균
total_avg = total_sum / 4

#각자 
temp = 0