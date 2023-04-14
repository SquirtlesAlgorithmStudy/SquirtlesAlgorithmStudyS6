price = int(input())

change = 1000 - price
cnt_500 = change // 500
change = change % 500
cnt_100 = change // 100
change = change % 100
cnt_50 = change // 50
change = change % 50
cnt_10 = change // 10
change = change % 10
cnt_5 = change // 5
change = change % 5
cnt_1 = change // 1

total_cnt = cnt_500 + cnt_100 + cnt_50 + cnt_10 + cnt_5 + cnt_1
print(total_cnt)