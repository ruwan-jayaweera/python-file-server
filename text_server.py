import socket


def main():
    s = socket.socket()
    s.bind(("127.0.0.1", 3000))

    s.listen(2)
    c, address = s.accept();
    print("received connection from :" + str(address))
    while True:
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print("data received:" + str(data))

        c.send(data.encode().upper())
    c.close()


if __name__ == '__main__':
    main()
