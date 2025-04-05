import requests

def check_token_validity(token):
    headers = {'Authorization': token}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    return response.status_code == 200

def get_user_info(token):
    headers = {'Authorization': token}
    response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    if response.status_code == 200:
        return response.json()
    return None