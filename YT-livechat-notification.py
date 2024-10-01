import pytchat
import pygame
import time
import threading
import keyboard
from rich.console import Console
from rich.text import Text

# Inisialisasi console rich
console = Console()

# Menampilkan watermark di bagian awal
watermark_text = Text("YouTube Live Chat Notification", style="bold blue")
author_text = Text("by: tobeoren", style="bold cyan")
volume_instructions = Text("Tekan '[' untuk mengecilkan volume, ']' untuk membesarkan volume.", style="italic white")

console.print(watermark_text, justify="center")
console.print(author_text, justify="center")
console.print(volume_instructions, justify="center")

# Fungsi untuk mengatur volume berdasarkan tombol yang ditekan
def adjust_volume():
    global volume
    while True:
        # Mengecek jika tombol '[' ditekan untuk mengecilkan volume
        if keyboard.is_pressed('['):
            volume = max(0.0, volume - 0.1)  # Mengecilkan volume 0.1, tidak kurang dari 0
            pygame.mixer.music.set_volume(volume)
            console.print(f"Volume diatur ke: {volume:.1f}", style="blue")
            time.sleep(0.5)  # Delay untuk menghindari perubahan volume berlebihan
        
        # Mengecek jika tombol ']' ditekan untuk membesarkan volume
        elif keyboard.is_pressed(']'):
            volume = min(1.0, volume + 0.1)  # Membesarkan volume 0.1, tidak lebih dari 1
            pygame.mixer.music.set_volume(volume)
            console.print(f"Volume diatur ke: {volume:.1f}", style="blue")
            time.sleep(0.5)  # Delay untuk menghindari perubahan volume berlebihan

# Memasukkan video_id dan kata textarea secara manual
video_id = input("Masukkan YouTube video_id: ")  # Contoh: DZ0hf7sKP4g

# Inisialisasi pygame untuk audio
pygame.mixer.init()
pygame.mixer.music.load('notifikasi.mp3')  # Pastikan path file audio benar

# Mengatur volume awal
volume = 0.5
pygame.mixer.music.set_volume(volume)

# Memulai thread untuk mengatur volume
volume_thread = threading.Thread(target=adjust_volume)
volume_thread.daemon = True  # Membuat thread sebagai daemon
volume_thread.start()

# Inisialisasi pytchat
chat = pytchat.create(video_id=video_id)

console.print("Menunggu chat baru...", style="green")

while chat.is_alive():
    for c in chat.get().sync_items():
        console.print(f"{c.author.name}: {c.message}", style="white")
        # Memutar notifikasi saat ada chat baru
        pygame.mixer.music.play()
        # Tunggu beberapa detik sebelum memeriksa lagi
        time.sleep(1)

    # Menunggu beberapa detik sebelum memeriksa lagi
    time.sleep(1)

# Menunggu thread volume selesai
volume_thread.join()
