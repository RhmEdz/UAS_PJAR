import socket
import os


from database import save_media,get_media



HOST="localhost"

PORT=8000



BASE_DIR=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



MEDIA_FOLDER=os.path.join(
    BASE_DIR,
    "storage",
    "media"
)



if not os.path.exists(MEDIA_FOLDER):

    os.makedirs(MEDIA_FOLDER)



server=socket.socket(
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



print(
    "MEDIA SERVER RUNNING"
)



while True:


    client,addr=server.accept()


    print(
        "Client:",
        addr
    )


    request=client.recv(1024).decode()



    if request.startswith("UPLOAD_MEDIA"):


        data=request.split("|")


        filename=data[1]

        media_type=data[2]

        owner=data[3]



        filepath=os.path.join(
            MEDIA_FOLDER,
            filename
        )



        file=open(
            filepath,
            "wb"
        )



        while True:


            chunk=client.recv(4096)


            if b"<END>" in chunk:


                chunk=chunk.replace(
                    b"<END>",
                    b""
                )


                file.write(chunk)

                break



            file.write(chunk)



        file.close()



        save_media(

            filename,

            filepath,

            media_type,

            owner

        )



        client.send(
            b"MEDIA UPLOAD SUCCESS"
        )



    elif request=="REFRESH_MEDIA":


        media=get_media()


        client.send(
            str(media).encode()
        )



    client.close()