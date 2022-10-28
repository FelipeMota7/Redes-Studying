import socket

from distutils.log import error


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #método para bind, abrindo as tupulas para colocar em que endereço o servidor vai escutar, seguido da porta
    server.bind(("0.0.0.0", 1144))
    server.listen(5)
    print("Escutando!")

    client_socket, address = server.accept()
    print("Received from: " + address[0])

    while True:
        data = client_socket.recv(1023).decode()
        if data == "código\n":
            client_socket.send(b"liberado")
        


except Exception as erros:
    print("Erro: ", error)
    server.close()