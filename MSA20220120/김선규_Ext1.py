score_1 = [95, 90, 80 , 50]
score_2 = [100, 50, 90, 90]
score_3 = [99, 60, 100, 40]
score_4 = [55, 80, 80, 60]

#각자 합
sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0

for i in score_1:
    sum_1 += i

for i in score_2:
    sum_2 += i

for i in score_3:
    sum_3 += i

for i in score_4:
    sum_4 += i

#각자 평균
avg_1 = sum_1 / 4
avg_2 = sum_2 / 4
avg_3 = sum_3 / 4
avg_4 = sum_4 / 4

#전체 합
total_sum = sum_1 + sum_2 + sum_3 + sum_4

#전체 평균
total_avg = (avg_1 + avg_2 + avg_3 + avg_4) / 4

temp = 0