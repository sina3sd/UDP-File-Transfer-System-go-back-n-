import socket

def receiver():
    # ایجاد سوکت UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # مشخص کردن آدرس و پورت گیرنده
    receiver_address = "localhost"
    receiver_port = 12345

    # بایند سوکت به آدرس و پورت گیرنده
    sock.bind((receiver_address, receiver_port))

    # دریافت بسته‌ها
    while True:
        data, addr = sock.recvfrom(1024)
        print("Received packet from:", addr)
        print("Data:", data.decode())

    sock.close()

# فراخوانی تابع گیرنده
receiver()