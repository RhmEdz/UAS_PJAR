import socket
import os


SERVER = "localhost"
PORT = 5000



# ==========================
# UPLOAD FILE
# ==========================

def upload_file(filepath, email):


    filename = os.path.basename(filepath)


    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )


    client.connect(
        (
            SERVER,
            PORT
        )
    )


    command = (
        f"UPLOAD|{filename}|{email}"
    )


    client.send(
        command.encode()
    )


    file = open(
        filepath,
        "rb"
    )


    while True:


        data = file.read(4096)


        if not data:

            break


        client.sendall(data)



    file.close()



    # tanda selesai
    client.sendall(
        b"<END>"
    )



    response = client.recv(1024).decode()


    print(
        response
    )


    client.close()





# ==========================
# REFRESH FILE
# ==========================

def refresh_file():


    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )


    client.connect(
        (
            SERVER,
            PORT
        )
    )


    client.send(
        b"REFRESH"
    )



    data = client.recv(4096).decode()



    print("\n===== LIST FILE =====")

    print(data)



    client.close()





# ==========================
# DOWNLOAD FILE
# ==========================

def download_file(filename):


    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )


    client.connect(
        (
            SERVER,
            PORT
        )
    )



    command = (
        f"DOWNLOAD|{filename}"
    )


    client.send(
        command.encode()
    )



    save_name = (
        "download_" + filename
    )


    file = open(
        save_name,
        "wb"
    )



    while True:


        data = client.recv(4096)


        if b"<END>" in data:


            data = data.replace(
                b"<END>",
                b""
            )


            file.write(data)

            break



        file.write(data)



    file.close()



    print(
        "DOWNLOAD SUCCESS:",
        save_name
    )



    client.close()





# ==========================
# MENU PROGRAM
# ==========================

while True:


    print(
        """
========================

TCP FILE TRANSFER

1. Upload File
2. Refresh File
3. Download File
4. Exit

========================
"""
    )



    choice = input(
        "Pilih menu: "
    )



    if choice == "1":


        path = input(
            "Masukkan lokasi file: "
        )


        email = input(
            "Email user: "
        )


        upload_file(
            path,
            email
        )



    elif choice == "2":


        refresh_file()



    elif choice == "3":


        filename = input(
            "Nama file yang di download: "
        )


        download_file(
            filename
        )



    elif choice == "4":


        print(
            "Program selesai"
        )

        break



    else:


        print(
            "Menu tidak tersedia"
        )