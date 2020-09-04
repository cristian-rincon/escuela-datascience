def greedy_change(res, coins, client_coins):
    if res == 0:
        return client_coins
    else:
        for key, value in coins.items():
            if res >= key and value > 0:
                client_coins[key] += 1
                coins[key] = value - 1
                res -= key
                break

        greedy_change(res, coins, client_coins)


if __name__ == "__main__":

    while True:
        amount = int(input('Total amount: '))
        payment = int(input('Customer payment: '))

        res = payment - amount

        coins = {
            20: 4,
            10: 5,
            5: 10,
            1: 3
        }

        total_money = 0
        for key, value in coins.items():
            total_money += (key * value)
        if amount > payment:
            print('------------------------------------------------------------------')
            print('The customer\'s payment must be greater than the amount to be paid')
            print('------------------------------------------------------------------')

        elif total_money < res:
            print('----------------')
            print('Not enough money. Go with the supervisor for more money.')
            print('----------------')
        else:
            client_coins = coins.copy()

            for key, value in client_coins.items():
                client_coins[key] = 0

            greedy_change(res, coins, client_coins)

            result = []

            for key, value in client_coins.items():
                if value > 0:
                    result.append(f'{value} coins of ${key} pesos')

            print('Return to customer:\n')
            for i in result:
                print(f'    {i}')
            print(f'\n    Total: ${res}')
            exit()
