import os
import time
from multiprocessing import Process

# Fungsi yang dijalankan oleh proses anak
def child_process():
    pid = os.getpid()  # Mendapatkan ID proses anak
    print(f"Proses anak {pid} sedang berjalan")
    time.sleep(5)  # Simulasi kerja
    print(f"Proses anak {pid} selesai")

# Fungsi untuk memulai proses
def fork_process():
    # Buat dan jalankan proses anak
    process = Process(target=child_process)
    process.start()

    # Proses induk menunggu proses anak selesai
    print(f"Proses induk {os.getpid()} menunggu proses anak {process.pid}")
    process.join()  # Menunggu proses anak selesai
    print("Proses induk selesai.")

# Panggil fungsi untuk memulai proses
if __name__ == "__main__":
    fork_process()