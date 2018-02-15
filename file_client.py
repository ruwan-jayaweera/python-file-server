import socket


def main():
    s = socket.socket()
    s.connect(("127.0.0.1", 3000))

    file_name = input(">>>")
    while file_name != 'q':
        try:
            f = open(file_name, "rb")
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)
            f.close()
        except FileNotFoundError:
            print("No file found")
        file_name = input(">>>")
    s.close()


if __name__ == "__main__":
    main()
