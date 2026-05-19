ipv4_address = input("Enter a IPv4 address to Validate: ")
fields = ipv4_address.split('.')

if len(fields) != 4:
    print("INVALID")
    exit(0)
else:
    for field in fields:
        if not field.isdigit():
            print("INVALID")
            exit(0)
        if int(field) < 0 or int(field) > 255:
            print("INVALID")
            exit(0)
    print(f"{ipv4_address} is VALID")
    
