import requests
import json

print("=== JokeAPI Client для практики ===")

# Эндпоинт 1: Случайная шутка (без ограничений)
response = requests.get("https://v2.jokeapi.dev/joke/Any")
if response.status_code == 200:
    joke = response.json()
    if joke["type"] == "single":
        print("Шутка:", joke["joke"])
    else:
        print("Setup:", joke["setup"])
        print("Delivery:", joke["delivery"])
else:
    print("Ошибка запроса:", response.status_code)

# Эндпоинт 2: Шутка в категории Programming с blacklist
params = {
    "type": "single",
    "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit"
}
prog_response = requests.get("https://v2.jokeapi.dev/joke/Programming", params=params)
print("\nПрограммистская шутка:")
print(prog_response.json().get("joke", "Нет шутки"))

# Сохраняем результат
result = {
    "random_joke": joke,
    "programming_joke": prog_response.json()
}
with open("jokes_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("\nРезультаты сохранены в jokes_result.json")