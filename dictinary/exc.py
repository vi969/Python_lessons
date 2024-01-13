import sys

# Формируем словарь.
movie = {
    "name": sys.argv[1],
    "rating": float(sys.argv[2]),
    "votes": int(sys.argv[3])
}

m_template = "{m[name]} ({m[rating]:.1f})"

# Форматируем строку данными из словаря.
print(m_template.format(m=movie))
