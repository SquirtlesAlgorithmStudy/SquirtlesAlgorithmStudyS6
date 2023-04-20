price = int(input())
change = 1000 - price 
total_cnt = 0

coins = [500,100,50,10,5,1]

for coin in coins: 
    total_cnt += change // coin
    change %= coin
    
    
print(total_cnt)