import socket

host = "google.com.br"
ports = [21, 22, 23, 25, 80, 443, 445, 8080, 844, 3306, 139, 135]

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((host, port))
    if code == 0:
        print("[+] {} open".format(port))
    