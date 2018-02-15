import socket


def main():
    s = socket.socket()
    s.connect(("127.0.0.1", 3000))

    msg = input(">>>")
    while msg != 'q':
        s.send(msg.encode())
        data = s.recv(1024)
        print(str(data.decode()))
        msg = input(">>>")
    s.close()


if __name__ == "__main__":
    main()
