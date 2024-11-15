amount = int(input())
dis_10 = 0.1 * amount
dis_100 = 100
dis=max(dis_10,dis_100)
total=amount-dis
print(int(total))
