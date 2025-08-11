import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        print(f"{ip} is a valid IP address.")
        return True
    except ValueError:
        print(f"{ip} is not a valid IP address.")
        return False

while True:
    ip_address = input("Enter an IP address or type 'quit' to quit: \n").strip()
    if ip_address.lower() == 'quit':
        break
    if not ip_address:
        print("IP address cannot be empty.")
        continue
    validate_ip(ip_address)
