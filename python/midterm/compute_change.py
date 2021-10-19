def solution(money: int):
    bill = 1000
    remain = bill - money
    coin = [500, 100, 50, 10, 1]
    get_coin = {}
    for i in coin:
        cnt = remain // i
        get_coin[i] = cnt
        remain -= i * cnt

    for _coin, _num in get_coin.items():
        if _num > 0:
            print(f'[{_coin}]: {_num}', end='\n')
    print(f'total_coin_num: {sum(get_coin.values())}')


if __name__ == '__main__':
    _input = 456
    solution(_input)
