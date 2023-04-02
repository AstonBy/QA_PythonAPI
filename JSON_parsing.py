import json

string_as_json_format = '{"answer": "Hello, AST", "answer2": "Hello to You", "rrrr": "yyyy"}'
print(string_as_json_format)

obj = json.loads(string_as_json_format)
print(obj)
key = "answer5"

if key in obj:
    print(obj[key])
else:
            print(f"Ключа {key} в JSON нет")

key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")

key = "rrrr"
if key in obj:
        print(obj[key])
else:
        print(f"Ключа {key} в JSON нет")