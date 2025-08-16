def change_making_dp(_coin_list, _amount):
    min_coins_list = [0] * (_amount + 1)
    for i in range(1, _amount + 1):
        min_coins = float('inf')
        new_coin_list = [c for c in _coin_list if c <= i]
        if not new_coin_list:
            min_coins_list[i] = -1
            continue
        found_solution = False
        for c in new_coin_list:
            _res = min_coins_list[i - c]
            if _res > -1:
                coins_used = 1 + min_coins_list[i - c]
                found_solution = True
            else:
                continue
            if coins_used < min_coins:
                min_coins = coins_used
        if found_solution:
            min_coins_list[i] = min_coins
        else:
            min_coins_list[i] = -1
    return min_coins_list[_amount]


if __name__ == '__main__':
    amount = 4
    coin_list = [5, 10, 21]
    res = change_making_dp(coin_list, amount)
    print(res)
