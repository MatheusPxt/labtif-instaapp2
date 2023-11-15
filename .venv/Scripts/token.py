from instagram_private_api import Client, ClientCompatPatch

def get_access_token(username, password):
    api = Client(username, password)
    user_id = api.authenticated_user_id
    access_token = api.generate_uuid()
    return user_id, access_token

def get_user_data(api, user_id):
    user_info = api.user_info(user_id)
    return user_info

if __name__ == '__main__':
    # Substitua 'YOUR_USERNAME' e 'YOUR_PASSWORD' pelas suas credenciais do Instagram
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'

    user_id, access_token = get_access_token(username, password)

    api = Client(username, password, user_id=user_id, authenticated_user_id=user_id)
    ClientCompatPatch(api)

    user_data = get_user_data(api, user_id)
    print(user_data)