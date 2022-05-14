def max_profit(price_list, count):
    profit_table = [0]
    # 개수 1부터 count까지 계산하기 위해 반복문
    for i in range(1, count + 1):
        # 새꼼달꼼 i개에 대한 최대 수익을 담는 변수 profit
        # i개에 대한 가격이 price_list에 있으면,
        # profit에 price_list[i]값을 넣는다
        # i개에 대한 가격이 price_list에 없으면,
        # profit에 0을 넣는다
        profit = price_list[i] if i < len(price_list) else 0

        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)


    return profit_table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
