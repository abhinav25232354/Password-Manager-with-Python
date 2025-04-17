import json
import ACCESS_GRANTED
import data
import shutil

def printf(text):
    # Get the terminal size
    terminal_width = shutil.get_terminal_size().columns
    
    # Split text into lines in case it's multi-line
    lines = text.split('\n')
    
    for line in lines:
        # Calculate the padding on the left to center the text
        padding = (terminal_width - len(line)) // 2
        centered_line = ' ' * padding + line
        print(centered_line)

# Open the JSON file and load its content
for i in range(0, 1, 1):
    with open('data.json', 'r') as file:
        load = json.load(file)

    password = load['password']
    user = input("Enter Passkey to access confidential information\n> ")

    if user == password:
        printf("Password access granted\n")
        ACCESS_GRANTED.Welcome()
        data.access_point_key()
        input()

    else:
        printf("Access denied")
        input()
        f = open("Denied_Access.txt", "a")
        f.write(user + "\n")
    
print("Feedback Saved")