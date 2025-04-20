import os
import sqlite3
import pickle
import json

USERNAME = "admin"
PASSWORD = "1234"

def login(user, pwd):
    if user == USERNAME and pwd == PASSWORD:
        return True
    return False

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def run_system_command(user_input):
    os.system("echo " + user_input)

def calculate_expression(expr):
    return eval(expr)

def load_user_settings(pickled_data):
    return pickle.loads(pickled_data)

def print_message(message):
    print("User says: " + message)

# Example usage
if __name__ == "__main__":
    user = input("Username: ")
    pwd = input("Password: ")
    if login(user, pwd):
        print("Logged in.")
        name = input("Enter username to lookup: ")
        print(get_user_data(name))

        cmd = input("Run a system command: ")
        run_system_command(cmd)

        expr = input("Math expression to evaluate: ")
        print("Result:", calculate_expression(expr))

        pickled = input("Paste pickled user settings (base64-encoded): ")
        try:
            import base64
            settings = load_user_settings(base64.b64decode(pickled))
            print("Settings loaded:", settings)
        except Exception as e:
            print("Failed to load settings:", e)

        msg = input("Enter a message: ")
        print_message(msg)
    else:
        print("Login failed.")
