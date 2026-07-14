from flask import Flask, render_template, request, redirect, session, Response

import os
import socket
import random
import smtplib
import time
from flask import send_file
from email.message import EmailMessage

import mysql.connector



app = Flask(__name__)

app.secret_key = "network_project"

TCP_HOST="localhost"
TCP_PORT=5000


# penyimpanan OTP sementara
otp_storage = {}

network_logs = [
    "TCP SERVER LOG",
    "Waiting Client...",
    "Ready Receive File..."
]

# ==========================
# DATABASE
# ==========================

def connect_db():

    db = mysql.connector.connect(

        host="localhost",

        user="root",

        password="",

        database="pjar"

    )

    return db




# ==========================
# LOGIN PAGE
# ==========================

@app.route("/")
@app.route("/login")
def login_page():

    return render_template(
        "login.html"
    )





# ==========================
# LOGIN PROCESS
# ==========================

@app.route("/login", methods=["POST"])
def login_process():


    email = request.form["email"]

    password = request.form["password"]



    db = connect_db()

    cursor = db.cursor()



    query = """
    SELECT * FROM users
    WHERE email=%s
    AND password=%s
    AND verified=TRUE
    AND permission=TRUE
    """



    cursor.execute(

        query,

        (
            email,
            password
        )

    )


    user = cursor.fetchone()



    cursor.close()

    db.close()



    if user:


        session["email"] = email


        return redirect(
            "/dashboard"
        )


    else:


        return "LOGIN GAGAL - Email belum diverifikasi atau tidak punya permission"





# ==========================
# REGISTER PAGE
# ==========================

@app.route("/register")
def register():


    return render_template(
        "register.html"
    )






# ==========================
# REGISTER PROCESS
# ==========================

@app.route("/register", methods=["POST"])
def register_process():


    email=request.form["email"]

    password=request.form["password"]



    otp=str(
        random.randint(
            100000,
            999999
        )
    )



    otp_storage[email]=otp



    send_otp(
        email,
        otp
    )



    session["email"]=email

    session["password"]=password



    return redirect(
        "/verify"
    )





# ==========================
# VERIFY PAGE
# ==========================

@app.route("/verify")
def verify():


    return render_template(
        "verify.html"
    )





# ==========================
# VERIFY PROCESS
# ==========================

@app.route("/verify", methods=["POST"])
def verify_process():


    otp=request.form["otp"]


    email=session["email"]

    password=session["password"]



    if otp_storage[email] == otp:



        db=connect_db()

        cursor=db.cursor()



        query="""

        INSERT INTO users
        (email,password,permission,verified)

        VALUES
        (%s,%s,%s,%s)

        """



        cursor.execute(

            query,

            (
                email,
                password,
                True,
                True
            )

        )



        db.commit()



        cursor.close()

        db.close()



        return redirect(
            "/login"
        )



    else:


        return "OTP SALAH"





# ==========================
# DASHBOARD
# ==========================

@app.route("/dashboard")
def dashboard():


    if "email" not in session:


        return redirect(
            "/login"
        )


    return render_template(
        "dashboard.html",
        logs=network_logs
    )


@app.route("/upload")
def upload_page():

    return render_template(
        "upload.html"
    )

# ==========================
# UDP STREAMING
# ==========================

from flask import Response


def generate_frames():

    while True:

        # sementara kosong
        # nanti diisi data frame dari UDP server

        frame = b''


        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + frame +
            b'\r\n'
        )



@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype=
        "multipart/x-mixed-replace; boundary=frame"
    )

# ==========================
# UPLOAD FILE TCP
# ==========================

@app.route("/upload_file", methods=["POST"])
def upload_file_web():


    file = request.files["file"]


    filepath = os.path.join(
        "uploads",
        file.filename
    )


    file.save(filepath)



    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )



    client.connect(
        (
            TCP_HOST,
            TCP_PORT
        )
    )



    command = (
        f"UPLOAD|{file.filename}|{session['email']}"
    )



    client.sendall(
        command.encode()
    )


    time.sleep(0.1)



    # kirim ukuran file

    filesize = os.path.getsize(
        filepath
    )


    client.sendall(
        str(filesize).encode()
    )



    time.sleep(0.1)



    # kirim isi file

    f = open(
        filepath,
        "rb"
    )



    while True:


        data = f.read(4096)


        if not data:
            break


        client.sendall(data)



    f.close()



    response = client.recv(1024).decode()

    network_logs.append(
        "Client Connected"
    )


    network_logs.append(
        f"File Uploaded: {file.filename}"
    )


    network_logs.append(
        "TCP Transfer Success"
    )

    client.close()


    return redirect("/dashboard?status=success")

# ==========================
# REFRESH FILE TCP
# ==========================

@app.route("/refresh_file")
def refresh_file():


    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )


    client.connect(
        (
            TCP_HOST,
            TCP_PORT
        )
    )



    client.send(
        b"REFRESH"
    )



    data = client.recv(4096).decode()



    client.close()



    return render_template(
        "file_list.html",
        files=data.split("----------------------")
    )

# ==========================
# DOWNLOAD FILE TCP
# ==========================

@app.route("/download")
@app.route("/download/")
def download_page():

    return render_template(
        "download.html"
    )

@app.route("/download_file", methods=["POST","GET"])
def download_file():


    if request.method=="POST":

        filename=request.form["filename"]

    else:

        filename=request.args.get("filename")



    client=socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.connect(
        (
            TCP_HOST,
            TCP_PORT
        )
    )



    client.send(
        f"DOWNLOAD|{filename}".encode()
    )



    save_path=os.path.join(
        "uploads",
        "download_"+filename
    )



    file=open(
        save_path,
        "wb"
    )



    while True:


        data=client.recv(4096)


        if not data:

            break


        file.write(data)



    file.close()


    client.close()



    return send_file(
        save_path,
        as_attachment=True
    )
# ==========================
# SMTP OTP
# ==========================

def send_otp(receiver, otp):


    msg = EmailMessage()


    msg["Subject"] = "OTP Verification"


    msg["From"] = "vrohim1907@gmail.com"


    msg["To"] = receiver



    msg.set_content(

        f"""

        Kode OTP anda:

        {otp}

        """

    )



    server=smtplib.SMTP(

        "smtp.gmail.com",

        587

    )


    server.starttls()



    server.login(

        "vrohim1907@gmail.com",

        "rpsd qtll fpom xxqd"

    )



    server.send_message(msg)


    server.quit()





app.run(

    host="localhost",

    port=8080,

    debug=True

)

