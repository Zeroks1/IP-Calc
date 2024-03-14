import ipaddress
import os

# ANSI escape codes for colors
yellow_color = "\033[93m"
red_color = "\033[91m"

def calculate_ip_parameters(ip, subnet):
    try:
        ip_network = ipaddress.ip_interface(ip + '/' + str(subnet)).network
        network_address = ip_network.network_address
        broadcast_address = ip_network.broadcast_address
        first_host = network_address + 1
        last_host = broadcast_address - 1
    except ValueError:
        return red_color + "Invalid Subnet Mask. Please enter a valid subnet mask.", None

    return None, {
        "IP Address": ip,
        "Subnet Mask": str(ip_network.netmask),
        "Network Address": str(network_address),
        "Broadcast Address": str(broadcast_address),
        "First Host Address": str(first_host),
        "Last Host Address": str(last_host)
    }

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    os.system('color') # enable ANSI escape codes for Windows terminal
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # clear terminal screen
        print(yellow_color) # set text color to yellow
        
        ip = input("Enter IP Address (or type 'exit' to quit): ")
        
        if ip.lower() == 'exit':
            break
        
        subnet = int(input("Enter Subnet Mask (CIDR Notation, e.g., 24): "))
        
        error_message, parameters = calculate_ip_parameters(ip, subnet)
        if error_message:
            print(error_message)
            input("Press Enter to continue...")
            continue

        for key, value in parameters.items():
            print(f"{key}: {value}")

        input("Press Enter to continue...")
