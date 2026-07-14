import socket

import random

import smtplib

from email.message import EmailMessage


from database import register_user, login_user

from config.config import *




def send_email_otp(receiver):


    otp=str(random.randint(100000,999999))


    msg=EmailMessage()


    msg["Subject"]="OTP Registration"

    msg["From"]=SMTP_USERNAME

    msg["To"]=receiver



    msg.set_content(

        f"""

        Your OTP Code:

        {otp}

        """

    )



    server=smtplib.SMTP(

        SMTP_HOST,

        SMTP_PORT

    )


    server.starttls()



    server.login(

        SMTP_USERNAME,

        SMTP_PASSWORD

    )



    server.send_message(msg)


    server.quit()



    return otp






server_socket=socket.socket(

    socket.AF_INET,

    socket.SOCK_STREAM

)



server_socket.bind(

    (AUTH_HOST,AUTH_PORT)

)



server_socket.listen(5)



print("AUTH SERVER RUNNING")





while True:


    client,addr=server_socket.accept()


    print(

        "Client connected:",

        addr

    )



    data=client.recv(1024).decode()



    command=data.split("|")



    if command[0]=="REGISTER":


        email=command[1]

        password=command[2]



        otp=send_email_otp(email)



        client.send(

            "OTP SENT".encode()

        )



        user_otp=client.recv(1024).decode()



        if user_otp==otp:


            register_user(

                email,

                password

            )


            client.send(

                "REGISTER SUCCESS".encode()

            )

        else:


            client.send(

                "OTP FAILED".encode()

            )





    elif command[0]=="LOGIN":


        email=command[1]

        password=command[2]



        status=login_user(

            email,

            password

        )


        if status:


            client.send(

                "LOGIN SUCCESS".encode()

            )


        else:


            client.send(

                "LOGIN FAILED".encode()

            )



    client.close()