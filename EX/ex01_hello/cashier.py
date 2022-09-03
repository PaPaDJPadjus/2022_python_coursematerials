"""Raha."""
money = int(input("Enter a sum: "))
coins = 0

cha50 = money // 50
coins = coins + cha50
money = money % 50

cha20 = money // 20
coins = coins + cha20
money = money % 20

cha10 = money // 10
coins = coins + cha10
money = money % 10

cha5 = money // 5
coins = coins + cha5
money = money % 5

cha1 = money // 1
coins = coins + cha1

print(f"Amount of coins needed: {coins}")
