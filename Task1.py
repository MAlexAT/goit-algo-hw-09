import time

# Жадібний алгоритм для видачі решти
def find_coins_greedy(amount, coins):
    coins = sorted(coins, reverse=True)  # Сортуємо номінали від більшого до меншого
    result = {}
    for coin in coins:
        count = amount // coin  # Визначаємо кількість монет даного номіналу
        if count > 0:
            result[coin] = count
            amount -= coin * count  # Зменшуємо залишок
    return result

# Динамічне програмування для видачі решти
def find_min_coins(amount, coins):
    # Ініціалізація масивів для зберігання мінімальної кількості монет і їхніх комбінацій
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_count = [{} for _ in range(amount + 1)]
    
    # Основний цикл для розрахунку мінімальної кількості монет для кожної суми
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                coin_count[i][coin] = coin_count[i].get(coin, 0) + 1

    return coin_count[amount]

# Приклади для тестування
coins = [50, 25, 10, 5, 2, 1]
amount = 113

# Вимірюємо час виконання жадібного алгоритму
start_time = time.time()
greedy_result = find_coins_greedy(amount, coins)
end_time = time.time()
greedy_time = end_time - start_time

# Вимірюємо час виконання алгоритму динамічного програмування
start_time = time.time()
dp_result = find_min_coins(amount, coins)
end_time = time.time()
dp_time = end_time - start_time

# Виведення результатів
print("Жадібний алгоритм:")
print("Результат:", greedy_result)
print("Час виконання:", greedy_time, "секунд")

print("\nДинамічне програмування:")
print("Результат:", dp_result)
print("Час виконання:", dp_time, "секунд")
