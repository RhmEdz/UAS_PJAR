import socket
import cv2
import pickle
import struct
import time



HOST = "localhost"
PORT = 6000



server = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)



server.bind(
    (
        HOST,
        PORT
    )
)



print("UDP VIDEO STREAM SERVER RUNNING")



# lokasi video

VIDEO_PATH = "../storage/media/video2.mp4"



video = cv2.VideoCapture(
    VIDEO_PATH
)



if not video.isOpened():

    print(
        "Video gagal dibuka:",
        VIDEO_PATH
    )

    exit()



print("Video berhasil dibuka")



client_address = None



while True:


    # menunggu client

    if client_address is None:


        message, address = server.recvfrom(
            1024
        )


        if message == b"START":


            print(
                "START diterima"
            )


            client_address = address


            print(
                "Client Connected:",
                client_address
            )



    # ambil frame video

    ret, frame = video.read()


    if not ret:

        print(
            "Video restart"
        )

        video.set(
            cv2.CAP_PROP_POS_FRAMES,
            0
        )

        continue



    # kecilkan resolusi

    frame = cv2.resize(
        frame,
        (640,360)
    )



    # kompres JPEG

    result, encoded = cv2.imencode(
        ".jpg",
        frame,
        [
            cv2.IMWRITE_JPEG_QUALITY,
            50
        ]
    )


    if not result:

        continue



    # ubah menjadi bytes

    data = pickle.dumps(
        encoded
    )



    # kirim ukuran data dulu

    message_size = struct.pack(
        "L",
        len(data)
    )



    packet = (
        message_size +
        data
    )



    if client_address:


        print(
            "Packet size:",
            len(packet)
        )


        server.sendto(
            packet,
            client_address
        )
        


        print(
            "Packet terkirim"
        )

        time.sleep(0.03)



video.release()

server.close()


print(
    "UDP SERVER STOPPED"
)