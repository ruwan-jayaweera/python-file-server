import socket
import uuid


def main():
    s = socket.socket()
    s.bind(("127.0.0.1", 3000))
    s.listen(2)
    c, address = s.accept()
    print("received connection from :" + str(address))
    while True:
        data = c.recv(1024)

        filename = str(uuid.uuid4())
        filename += ".jpg"
        f = open(filename, "wb")
        while data:
            f.write(data)
            print("data received:" + str(data))
            data = c.recv(1024)
        print("file received successfully")
        f.close()
    c.close()
    s.close()


if __name__ == '__main__':
    main()