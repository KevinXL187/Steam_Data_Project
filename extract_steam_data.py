import requests, os, json

API_KEY = os.getenv('STEAM_API_KEY')

def get_user_data():

    print('Enter Steam User ID:')
    steam_id = input()
    # Steam API Endpoint for getting owned games
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    params = f'?key={API_KEY}&steamid={steam_id}&format=json'

    response = requests.get(url+params)
    
    if response.status_code == 200:
        data = response.json()
        with open('steam_user_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    else: print(f"Failed to retrieve data. Status code: {response.status_code}")