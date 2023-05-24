# Ryan Mathews
# USask Network Programming Analyst
# This script will update a list of Cisco IOS appliances to configure the same batch of commands on each
# Version 1.0 - Basic Variable Creation
# Version 2.0 - Figuring out Netmiko as paramiko fucking sucks
# Version 3.0 - Abandoning executing commands over SSH and instead using just net_connect
# Ditching

import netmiko 
from netmiko import ConnectHandler

devices = [
    'ryanswitchtest.<Domain>.net'
]

# Prompt the user for credentials
username = input("NSID: ")
password = input("Password: ")

# Commands to execute on each device
commands = [
    'interface gigabitEthernet 2/0/3',
    'no description',
    'interface gigabiEthernet 2/0/3', #ISSUE: Even if commands are missspelled, the output still says they were all successful......
    'description fail'
# Add more commands here as needed
]

for device in devices:
    try:
        # Create a Netmiko connection handler for the device
        net_connect = ConnectHandler(
            device_type="cisco_ios",
            host=device,
            username=username,
            password=password,
        )
    
        # Enter global configuration mode
        net_connect.config_mode()

        # Execute the commands in global configuration mode
        output = net_connect.send_config_set(commands)

        # Check if all commands were executed successfully
        success_flag = True
        for command in commands:
            if command not in output:
                success_flag = False
                break

        # If all commands were executed successfully, print the output
        if success_flag:
            print(f"All commands executed successfully on {device}.") #ISSUE: Even if commands are missspelled, the output still says they were all successful......
        else:
            print(f"Not all commands were executed successfully on {device}.")

        # Exit global configuration mode
        net_connect.exit_config_mode()

        # Disconnect from the device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to {device}. Error: {str(e)}")