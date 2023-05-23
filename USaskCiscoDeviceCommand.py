# Ryan Mathews
# USask Network Programming Analyst
# This script will update a list of Cisco IOS appliances to configure the same batch of commands on each
# Version 2.0 - Figuring out Netmiko as paramiko fucking sucks

import netmiko 
from netmiko import ConnectHandler

devices = [
    'ryanswitchtest.usask.net'
]

# Prompt the user for credentials
username = input("Username: ")
password = input("Password: ")

# Commands to execute on each device
commands = [
    'conf t',
    'vlan 666',
#    'exit',
#    'interface vlan 666',
#    'description TEST',
    # Add more commands here as needed
]

# SSH connection parameters
ssh_params = {
    'device_type': 'cisco_ios',
    'username': username,
    'password': password,
}

# Loop through each device
for device in devices:
    print(f"\nConnecting to {device}...")
    ssh_params['host'] = device

    try:
        # Establish SSH connection
        ssh_conn = ConnectHandler(**ssh_params)

        # Execute commands on the device
        for command in commands:
            output = ssh_conn.send_command(command)
            print(f"\nCommand: {command}\n")
            print(output)

        # Close the SSH connection
        ssh_conn.disconnect()

        print(f"\nCommands executed successfully on {device}.")
    except Exception as e:
        print(f"\nUnable to connect to {device}. Error: {str(e)}")
        print(f"\n{device} SSH connection failed.")