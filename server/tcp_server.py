import socket
import os

from database import save_file, get_files


HOST = "localhost"
PORT = 5000


# =====================
# STORAGE LOCATION
# =====================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


STORAGE = os.path.join(
    BASE_DIR,
    "storage",
    "files"
)


if not os.path.exists(STORAGE):
    os.makedirs(STORAGE)



# =====================
# TCP SERVER
# =====================

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


server.bind(
    (
        HOST,
        PORT
    )
)


server.listen(5)


print("TCP SERVER RUNNING")



while True:


    client, address = server.accept()


    print(
        "Client Connected:",
        address
    )



    request = client.recv(1024).decode()



    # =====================
    # UPLOAD FILE
    # =====================

    if request.startswith("UPLOAD"):


        data = request.split("|")


        filename = data[1]

        owner = data[2]



        filepath = os.path.join(
            STORAGE,
            filename
        )



        print(
            "Receiving:",
            filename
        )



        # menerima ukuran file

        try:

            filesize = int(
                client.recv(1024).decode()
            )

        except:

            print("File size error")

            client.close()

            continue


        print(
            "File Size:",
            filesize,
            "bytes"
        )



        file = open(
            filepath,
            "wb"
        )



        received = 0



        while received < filesize:


            chunk = client.recv(4096)


            if not chunk:
                break



            file.write(chunk)


            received += len(chunk)



            print(
                "Received:",
                received,
                "/",
                filesize
            )



        file.close()



        save_file(
            filename,
            filepath,
            owner
        )



        print(
            "Saved:",
            filepath
        )



        client.send(
            b"UPLOAD SUCCESS"
        )




    # =====================
    # REFRESH FILE
    # =====================

    elif request == "REFRESH":


        files = get_files()


        response = ""


        for file in files:


            response += f"""

File  : {file[0]}
Path  : {file[1]}
Owner : {file[2]}
Time  : {file[3]}

----------------------

"""


        client.send(
            response.encode()
        )




    # =====================
    # DOWNLOAD FILE
    # =====================

    elif request.startswith("DOWNLOAD"):


        filename = request.split("|")[1]


        filepath = os.path.join(
            STORAGE,
            filename
        )



        if os.path.exists(filepath):


            print(
                "Sending:",
                filename
            )



            filesize = os.path.getsize(
                filepath
            )


            # kirim ukuran file dulu

            client.send(
                str(filesize).encode()
            )



            file = open(
                filepath,
                "rb"
            )



            sent = 0



            while True:


                data = file.read(4096)


                if not data:
                    break



                client.sendall(data)


                sent += len(data)



                print(
                    "Sending:",
                    sent,
                    "/",
                    filesize
                )



            file.close()



            print(
                "Download completed"
            )



        else:


            client.send(
                b"FILE NOT FOUND"
            )



    client.close()