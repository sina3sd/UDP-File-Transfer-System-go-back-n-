import socket

def sender():
    # ایجاد سوکت UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # دریافت اطلاعات از کاربر
    receiver_address = input("receiver address: ")
    receiver_port = int(input("receiver port: "))
    filename = input("file name: ")
    window_size = int(input("len: "))

    # بازکردن فایل برای ارسال
    file = open(filename, 'r')

    seq_num = 0
    packets = []

    # خواندن فایل به صورت بسته‌ها
    while True:
        data = file.read(window_size)
        if not data:
            break

        packets.append((seq_num, data))
        seq_num += 1

    file.close()

    # ارسال بسته‌ها به گیرنده
    for packet in packets:
        sock.sendto(packet[1].encode(), (receiver_address, receiver_port))
        print("Sent packet:", packet[0])

    sock.close()

# فراخوانی تابع ارسال
sender()