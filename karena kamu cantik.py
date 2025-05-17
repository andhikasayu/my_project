import time
import os

# Lirik lagu
lyrics = [
    "Karena kamu cantic",
    "Kan ku beri segalanya apa yang ku punya",
    "Dan hatimu baik",
    "Sempurnalah duniaku saat kau di sisiku",
    
    "Bukan karena make-up di wajahmu",
    "Atau lipstik merah itu",
    "Lembut hati, tutur kata",
    "Terciptalah cinta yang ku puja"
]

def typewriter_box(text, delay=0.05):
    box_width = len(text) + 4
    print("+" + "-" * box_width + "+")
    print("|  ", end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("  |")
    print("+" + "-" * box_width + "+")

# function
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎵 Lirik: Kamu Cantik Kamu Baik – Lyla 🎵\n")
    time.sleep(1)

    start_time = time.time()

    for line in lyrics:
        if line.strip() == "":
            print()
        else:
            typewriter_box(line)

            if line == "Dan hatimu baik":
                time.sleep(1)  # Tambahan delay khusus untuk baris ini

        time.sleep(1.8)  

    # Hitung total waktu
    end_time = time.time()
    duration = round(end_time - start_time)

    # Ending message
    print("code from: andhika sayu")
    print("\nKecepatan: 512 kbps")
    print(f"⏱Waktu: {duration} detik")
    print("Sukses menampilkan lirik!")
    print("Terima kasih!")

if __name__ == "__main__":
    main()
