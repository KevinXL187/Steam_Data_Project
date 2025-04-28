import json, ast

# reformating data
data1, data2 = [], []
with open("australian_users_items.json", 'r', encoding="utf8") as f:
    for line in f:
        line = line.strip()
        print(line)
        if line:
            user_data = ast.literal_eval(line)
            data1.append(user_data)
with open("steam_games.json", 'r', encoding="utf8") as f:
    for line in f:
        line = line.strip()
        print(line)
        if line:
            item_data = ast.literal_eval(line)
            data2.append(item_data)

with open('item_data.json', 'w', encoding='utf-8') as f:
    json.dump(data2, f,  indent=4, ensure_ascii=False)
with open('item_user_data.json', 'w', encoding='utf-8') as f:
    json.dump(data1, f,  indent=4, ensure_ascii=False)