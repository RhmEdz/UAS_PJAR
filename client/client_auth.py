import socket




SERVER="localhost"

PORT=7000




def connect_server(message):


    client=socket.socket(

        socket.AF_INET,

        socket.SOCK_STREAM

    )


    client.connect(

        (SERVER,PORT)

    )


    client.send(

        message.encode()

    )


    response=client.recv(1024).decode()



    print(response)



    return client






print("1. REGISTER")

print("2. LOGIN")



choice=input("Pilih: ")





if choice=="1":


    email=input("Email : ")

    password=input("Password : ")



    client=connect_server(

        f"REGISTER|{email}|{password}"

    )



    otp=input("Masukkan OTP : ")



    client.send(

        otp.encode()

    )


    print(

        client.recv(1024).decode()

    )





elif choice=="2":


    email=input("Email : ")

    password=input("Password : ")



    client=connect_server(

        f"LOGIN|{email}|{password}"

    )


    print(

        client.recv(1024).decode()

    )