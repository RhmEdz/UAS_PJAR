import socket
import os


SERVER = "localhost"

PORT = 8000



# ==========================
# UPLOAD MEDIA
# ==========================

def upload_media(filepath, email):


    filename = os.path.basename(filepath)


    media_type = os.path.splitext(filename)[1]



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
        f"UPLOAD_MEDIA|{filename}|{media_type}|{email}"
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



    client.sendall(
        b"<END>"
    )



    response = client.recv(1024).decode()



    print(response)



    client.close()





# ==========================
# REFRESH MEDIA
# ==========================

def refresh_media():


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
        b"REFRESH_MEDIA"
    )



    data = client.recv(4096).decode()



    print("\n===== LIST MEDIA =====")

    print(data)



    client.close()





# ==========================
# MENU
# ==========================


while True:


    print(
        """
=====================
MEDIA SYSTEM

1. Upload Media
2. Refresh Media
3. Exit

=====================
"""
    )



    choice=input(
        "Pilih menu: "
    )



    if choice=="1":


        path=input(
            "Lokasi media: "
        )


        email=input(
            "Email user: "
        )



        upload_media(
            path,
            email
        )



    elif choice=="2":


        refresh_media()



    elif choice=="3":


        break



    else:


        print(
            "Pilihan tidak ada"
        )