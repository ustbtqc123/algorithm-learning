def change_making_recursion(_coin_list, change, _known_list, _coin_used):
    min_coins = float('inf')

    # 如果金额恰好是某个硬币面值
    if change in _coin_list:
        _coin_used[change] = change
        _known_list[change] = 1
        return 1

    # 如果已经计算过（正数是结果，-1 表示无解）
    elif _known_list[change] != 0:
        return _known_list[change]

    # 如果金额小于最小硬币面值
    elif change < min(_coin_list):
        _coin_used[change] = -1
        _known_list[change] = -1
        return -1

    found_solution = False
    new_coin_list = [i for i in _coin_list if i <= change]
    for coin in new_coin_list:
        _res = change_making_recursion(_coin_list, change - coin, _known_list, _coin_used)
        if _res > -1:
            num_coins = 1 + _res
        else:
            continue
        found_solution = True
        if num_coins < min_coins:
            min_coins = num_coins
            _coin_used[change] = coin

    if found_solution:
        _known_list[change] = min_coins
        return min_coins
    else:
        _known_list[change] = -1
        _coin_used[change] = -1
        return -1


if __name__ == '__main__':
    amount = 63
    coin_list = [1, 5, 10, 21]
    known_list = [0] * (amount + 1)
    coin_used = [0] * (amount + 1)

    res = change_making_recursion(coin_list, amount, known_list, coin_used)

    if res == -1:
        print("无法用给定硬币组合成该金额")
    else:
        print(f"最少硬币数: {res}")
        while amount > 0 and coin_used[amount] > 0:
            print(coin_used[amount])
            amount -= coin_used[amount]

    print(known_list)
