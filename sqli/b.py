import os

def search_logs():
    keyword = input("Enter a keyword to search in logs: ")
    # Insecure usage: directly inserting user input into shell command
    command = f"grep '{keyword}' /var/log/syslog"
    os.system(command)

if __name__ == "__main__":
    search_logs()
