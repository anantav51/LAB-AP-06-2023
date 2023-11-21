import re

def IPv4(check):
    pattern = r'^((\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$'
    return re.search(pattern, check)

def IPv6(check):
    pattern = r'^([\da-f]{0,4}:){7}[\da-f]{0,4}[\da-f]{0,4}$'
    return re.search(pattern, check)

perulangan = int(input("Berapa kali anda ingin menginput? "))

var = []
for i in range(perulangan):
    var.append(input(f"Masukkan input ke {i + 1} : "))

for IP in var:
    if IPv4(IP):
        print("IPv4")
    elif IPv6(IP):
        print("IPv6")
    else:
        print("Bukan IP Address")