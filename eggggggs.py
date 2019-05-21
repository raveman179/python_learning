#coding:UTF-8
import time
import random
import sys

print("スーパーにやってきた。卵売り場はどこだろう？\n")

def Search_Eggs():
    #売り場を見つける判定の乱数と発見するまでの時間の乱数を分ける。未実装。
    past_time_search = random.randint(1, 20)
    TimeLimit = 15                            
    i = 0
    if past_time_search <= TimeLimit:         
        while i <= past_time_search:
            print("パック入りの卵を探している・・・・・・")
            time.sleep(1)
            i += 1
        print("卵売り場が見つかった。")
    elif past_time_search > TimeLimit:    
        while i <= TimeLimit:
            print("パック入りの卵を探している・・・・・・")
            time.sleep(1)
            i += 1
        print("時間になったから電話して！ 番号：XXX-XXXX-XXXX")
        sys.exit()

def BuyEggs():
    if egg_price >= 190:
        print("{0}個入りの卵1パックを買った。値段は{1}円だった。".format(eggs_quan, egg_price))
    elif egg_price <= 189:
        print("{0}個入りの卵1パックを買った。値段は{1}円だった。安く買えたようだ。".format(eggs_quan, egg_price))

Search_Eggs()

eggs_quan = int(input("1パックの卵は何個入り？"))
egg_price = int(input("1パックの値段は何円？"))

BuyEggs()

    