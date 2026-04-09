import json

def save_data(users_list):
    
    with open("users.json", "w") as f:
        json.dump(users_list, f, indent=4)
    
def load_data():

    try:
        with open("users.json", "r") as f:
            users_list = json.load(f)
    
        return users_list
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
