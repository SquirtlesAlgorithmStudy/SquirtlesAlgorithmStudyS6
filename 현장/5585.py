import sys

N = list(map(int,sys.stdin.readline().split()))

if __name__ == "__main__":
    
    N = N[0]

    origin = 1000
    coins = [500, 100, 50, 10, 5, 1]
    def search():

        default = origin - N
        count = 0
        while default:
            for coin in coins:
                if default >= coin:
                    count += 1
                    default -= coin
                    break

    search()

