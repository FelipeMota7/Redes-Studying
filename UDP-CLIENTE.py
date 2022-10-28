from http import client
import socket

try: 

    while True:

        msg = input ("Usuário: ") + "\n"
        client.sendto(msg.encode(), ("0.0.0.0", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break

    client.close()

except Exception as error:

    print("Erro")
    print(error)
    client.close()
