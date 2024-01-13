import sys

# Получаем данные.
model = sys.argv[1]
new_price = sys.argv[2]
new_count = float(sys.argv[2])

# Исходный словарь.
product = {
    "model": "UE43NU7097U",
    "brand": "Samsung",
    "price": 27990,
    "count": 7
}

# Обновляем данные.

product = product.update(Model=model, price=price)

# Выводим результат.
print(product)