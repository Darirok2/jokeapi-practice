import requests
import json

print("=== JokeAPI Client для практики ===\n")

# Список доступных категорий (тем)
categories = [
    "Any", "Programming", "Miscellaneous", "Dark", "Pun", 
    "Spooky", "Christmas"
]

print("Доступные категории шуток:")
for i, cat in enumerate(categories, 1):
    print(f"{i}. {cat}")

# Позволяем пользователю выбрать категорию
choice = input("\nВведите номер категории (или нажмите Enter для Any): ").strip()

if choice.isdigit() and 1 <= int(choice) <= len(categories):
    selected_category = categories[int(choice)-1]
else:
    selected_category = "Any"

print(f"\nВыбрана категория: {selected_category}\n")

# Основной запрос
url = f"https://v2.jokeapi.dev/joke/{selected_category}"

# Параметры для фильтрации (убираем нежелательный контент)
params = {
    "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    joke = response.json()
    
    if joke.get("error"):
        print("Ошибка от API:", joke.get("message"))
    elif joke["type"] == "single":
        print("Шутка:", joke["joke"])
    else:
        print("Setup:", joke["setup"])
        print("Delivery:", joke["delivery"])
else:
    print("Ошибка соединения:", response.status_code)

# Сохранение результата
result = {
    "category": selected_category,
    "joke": joke
}

with open("jokes_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("\nРезультат успешно сохранён в jokes_result.json")