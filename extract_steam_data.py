import requests, os, json

API_KEY = os.getenv('STEAM_API_KEY')

def get_user_data():
    print('Enter Steam User ID:')
    steam_id = input()
    # Steam API Endpoint for getting owned games
    url_owned_game = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    url_player_summary = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    params = f'?key={API_KEY}&steamid={steam_id}&format=json'

    response_owned_games = requests.get(url_owned_game+params)
    response_player_summary = requests.get(url_player_summary+params)
        
    if response_owned_games.status_code == 200 and response_player_summary == 200:
        data_og = response_owned_games.json()
        data_ps = response_player_summary.json()

        with open(f'steam_user_data ({steam_id}).json', 'w') as f:
            json.dump(data_ps, f, indent=4)
            json.dump(data_og, f, indent=4)

    else: print(f"Failed to retrieve data. Status code: {response_owned_games.status_code}")

def get_dic_Allapp():
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        apps = data['applist']['apps']

        app_dict = {app['appid']: app['name'] for app in apps}

        with open('steam_apps.json', 'w', encoding='utf-8') as f:
            json.dump(app_dict, f, indent=4, ensure_ascii=False)
    
    else: print(f"Failed to retrieve data. Status code: {response.status_code}")

def read_allApp():
    with open('steam_apps.json', 'r') as f:
        application_dictonary = json.load(f)

    return application_dictonary

def get_app_details(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        with open(f"steam_game_data ({app_id}),json", 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ =="__main__":
    get_user_data();


    
