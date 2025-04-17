import json

def access_point_key():
    with open('data.json', 'r') as file:
        load = json.load(file)

    password = load['password']
    print(f"Password : {password}")
    instagram = load['instagram']
    print(f"Instagram : {instagram}")
    facebook = load['facebook']
    print(f"Facebook : {facebook}")
    whatsapp = load['whatsapp']
    print(f"Whatsapp : {whatsapp}")
    print("\n")