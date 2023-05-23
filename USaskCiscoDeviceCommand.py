# Ryan Mathews
# USask Network Programming Analyst
# This script will update a list of Cisco IOS appliances to configure the same batch of commands on each
# Version 1.0 - Initial Creation

import paramiko

# List of FQDNs to connect
devices = [
    "fqdn1.example.com",
    "fqdn2.example.com",
    # Add more FQDNs to the list
]

# Prompt for credentials
username = input("Enter your username: ")
password = input("Enter your password: ")
