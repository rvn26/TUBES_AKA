import time
import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# data pasien
class Pasien:
    def __init__(self, nama, tingkat_prioritas):
        self.nama = nama
        self.tingkat_prioritas = tingkat_prioritas

# iteratif insertion sort
def prioritas_iteratif(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j].tingkat_prioritas > key.tingkat_prioritas:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# rekursif insertion sort
def prioritas_rekursif(data, n):
    if n <= 1:
        return
    # Urutkan elemen-elemen pertama (n-1)
    prioritas_rekursif(data, n - 1)
    # Sisipkan elemen terakhir ke posisi yang benar di bagian yang telah diurutkan
    last = data[n - 1]
    j = n - 2
    while j >= 0 and data[j].tingkat_prioritas > last.tingkat_prioritas:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = last

# Grafik untuk menyimpan data, Fungsi untuk memperbarui grafik, Fungsi untuk mencetak tabel waktu eksekusi
n_values = []
recursive_times = []
iterative_times = []

# Fungsi membuat grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, recursive_times, label='Rekursif', marker='o', linestyle='-', color='#212842')
    plt.plot(n_values, iterative_times, label='Iteratif', marker='o', linestyle='-', color='#C8D9E61')
    plt.title('Perbandingan Kinerja: Rekursif vs Iteratif')
    plt.xlabel('Input (n)')
    plt.ylabel('Waktu Eksekusi (detik)')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.01)

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Waktu Rekursif (s)", "Waktu Iteratif (s)"]
    # Gunakan panjang minimum dari semua daftar untuk menghindari IndexError
    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([n_values[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
while True:
    try:
        n = int(input("Masukkan jumlah pasien (atau ketik -1 untuk keluar): "))
        if n == -1:
            print("Program selesai. Terima kasih!")
            break
        if n < 0:
            print("Masukkan nilai n yang positif!")
            continue

        n_values.append(n)

        # Membuat daftar pasien acak dengan tingkat prioritas antara 1 dan 5
        pasien_list = [Pasien(f'Pasien {i+1}', random.randint(1, 5)) for i in range(n)]

        # Ukur waktu eksekusi algoritma rekursif
        start_time = time.time()
        prioritas_rekursif(pasien_list.copy(), n)
        recursive_times.append(time.time() - start_time)

        # Ukur waktu eksekusi algoritma iteratif
        start_time = time.time()
        prioritas_iteratif(pasien_list.copy())
        iterative_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan nilai n yang valid!")
