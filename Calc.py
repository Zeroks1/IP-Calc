import ipaddress
import os

# ANSI escape codes for colors
yellow_color = "\033[93m"
green_color = "\033[92m"
reset_color = "\033[0m"
red_color = "\033[91m"

def calculate_ip_parameters(ip, subnet):
    try:
        ip_address = ipaddress.ip_interface(ip + '/' + str(subnet))
        ip_network = ip_address.network
        network_address = ip_network.network_address
        broadcast_address = ip_network.broadcast_address
        first_host = network_address + 1
        last_host = broadcast_address - 1

        # Calculate the number of available hosts
        subnet_bits = 32 - subnet
        available_hosts = 2 ** subnet_bits - 2  # Subtracting network and broadcast addresses
        
        parameters = {
            "IP Address": colorize_numbers(ip),
            "Subnet Mask": colorize_numbers(str(ip_network.netmask)),
            "Network Address": colorize_numbers(str(network_address)),
            "Broadcast Address": colorize_numbers(str(broadcast_address)),
            "First Host Address": colorize_numbers(str(first_host)),
            "Last Host Address": colorize_numbers(str(last_host)),
            "Available Hosts": colorize_numbers(str(available_hosts))  # Colorize available hosts
        }

        return None, parameters

    except ValueError:
        return red_color + "Invalid IP Address. Please enter a valid IPv4 address.", None
    except:
        return red_color + "An unexpected error occurred.", None

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def colorize_numbers(string):
    colored_string = ""
    for char in string:
        if char.isdigit():
            colored_string += f"{green_color}{char}{reset_color}"
        else:
            colored_string += char
    return colored_string

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal screen
        print(yellow_color)  # set text color to yellow
        print()  # newline for clarity

        ip = input("Enter IP Address (or type 'exit' to quit): ")
        
        if ip.lower() == 'exit':
            break
        
        if not is_valid_ipv4(ip):
            print(red_color + "Invalid IP Address. Please enter a valid IPv4 address.")
            input("Press Enter to continue...")
            continue
        
        subnet = int(input("Enter Subnet Mask (CIDR Notation, e.g., 24): "))
        
        error_message, parameters = calculate_ip_parameters(ip, subnet)
        if error_message:
            print(error_message)
            input(red_color + "Press Enter to continue..." + reset_color)
            continue

        for key, value in parameters.items():
            print(f"{yellow_color}{key}:{reset_color} {value}")

        input(red_color + "Press Enter to continue..." + reset_color)
