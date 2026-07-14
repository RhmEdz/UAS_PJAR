import socket
import cv2
import pickle
import struct



SERVER = "localhost"
PORT = 6000



client = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)



print(
    "CONNECT UDP STREAM"
)



# request streaming

client.sendto(
    b"START",
    (
        SERVER,
        PORT
    )
)



data = b""


payload_size = struct.calcsize(
    "L"
)



while True:


    try:


        # menerima ukuran data

        while len(data) < payload_size:


            packet, addr = client.recvfrom(
                65536
            )


            data += packet



        packed_msg_size = data[:payload_size]


        data = data[payload_size:]


        msg_size = struct.unpack(
            "L",
            packed_msg_size
        )[0]



        # menerima isi frame

        while len(data) < msg_size:


            packet, addr = client.recvfrom(
                65536
            )


            data += packet



        frame_data = data[:msg_size]


        data = data[msg_size:]



        # decode JPEG

        encoded = pickle.loads(
            frame_data
        )



        frame = cv2.imdecode(
            encoded,
            cv2.IMREAD_COLOR
        )



        if frame is None:

            print(
                "Frame gagal decode"
            )

            continue



        cv2.imshow(
            "UDP VIDEO STREAM",
            frame
        )

        cv2.waitKey(30)



        # tekan q untuk keluar

        if cv2.waitKey(1) == ord("q"):

            break



    except ConnectionResetError:


        print(
            "Server UDP berhenti"
        )

        break



    except Exception as e:


        print(
            "Error:",
            e
        )

        break




client.close()


cv2.destroyAllWindows()


print(
    "UDP CLIENT STOPPED"
)