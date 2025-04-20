import os

ip_address = input("Enter the IP address to ping: ")

os.system("ping -c 1 " + ip_address)
