#################################################################
#                                                               #
#   TUGAS BESAR IMPLEMENTASI STUDI KASUS :                      #
#          1. Higher Order Function                             #
#               > lambda                                        #
#               > map                                           #
#               > filter                                        #
#               > sorted                                        #
#           2. Functools Module                                 #
#               > @lru_cache()                                  #
#               > partial()                                     #
#               > reduce()                                      #
#   IMPLEMENTASI STUDI KASUS DATA MATA KULIAH KELAS SIIF-07-O   #
#                                                               #
#################################################################

import functools
import operator
import os
from prettytable import PrettyTable

# element tuple :
# element 0 = presensi ----> bobot 10%
# element 1 = nilai tugas ---> bobot 30%
# element 2 = nilai UTS ---> bobot 25%
# element 3 = nilai UAS ----> bobot 35%

# data nilai presensi, tugas, uts, uas, nama mahasiswa
student_data = {
    (100, 70, 77, 90, "Hikmah"), (100, 85, 87, 90, "Kiel"), (100, 75, 80, 72, "Eleven"), (100, 86, 81, 75, "Shodik"), (100, 79, 75, 80, "Satrio"),
    (90, 85, 88, 75, "Fadh"), (100, 80, 89, 83, "Nanda"), (80, 70, 70, 87, "Wildan"), (100, 80, 77, 94, "Adel"), (100, 87, 78, 87, "Andriawan"),
    (100, 80, 80, 86, "Faishal"), (100, 71, 77, 86, "Yuri"), (100, 70, 71, 80, "Nafis"), (80, 75, 70, 89, "Lorance"), (85, 80, 72, 77, "Adi"),
    (100, 80, 73, 80, "Kaka"), (90, 75, 70, 85, "Hersa"), (100, 78, 76, 80, "Attar"), (100, 80, 72, 84, "Vindi"), (100, 85, 73, 72, "M Arif"),
    (100, 76, 80, 80, "Bagus"), (100, 74, 81, 87, "Fikri"), (100, 74, 83, 80, "Fahri"), (100, 79, 71, 81, "Herwin"), (100, 70, 78, 87, "Imam"),
    (100, 75, 76, 87, "Pandu"), (100, 78, 90, 70, "Risang"), (100, 80, 80, 86, "Ulinda"), (90, 75, 91, 85, "Salsa"), (95, 75, 92, 79, "Fakhri"),
    (100, 70, 80, 90, "Putri"), (100, 75, 81, 87, "Ma’arif"), (100, 73, 91, 85, "Martin"), (100, 76, 92, 72, "Galuh"), (100, 74, 81, 80, "Ihza"),
    (100, 70, 78, 80, "Rangga"), (80, 72, 81, 87, "Nurdin"), (85, 70, 90, 86, "Andika"), (80, 70, 91, 87, "Syifa"), (90, 70, 92, 88, "Bastian"),
    (100, 70, 90, 87, "Hafid"), (85, 70, 88, 82, "Maldini"), (80, 77, 81, 87, "Aldi"), (100, 76, 80, 80, "Regi"), (100, 76, 87, 80, "Annisa"),
    (100, 75, 92, 80, "Trias"), (100, 70, 91, 89, "Kevin"), (80, 70, 91, 87, "Atha")
}

# hitung nilai keseluruhan data
total_grade = sorted(list(map(lambda x: (((x[0] * 0.10) + (x[1] * 0.30) + (x[2] * 0.25) + (x[3] * 0.35)), x[4]), student_data)), reverse=True)

# jumlahkan semua nilai di total grade
jumlah = functools.reduce(operator.add, [x[0] for x in total_grade])

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# tampilkan data total_grade
def show_data(data_arg) :
    data_table = PrettyTable()
    data_table.field_names = ['Nama', 'Nilai']
    print('============== Data Nilai Akhir =============')
    t_grade = [[j, round(i, 1)] for i, j in data_arg]
    for i in t_grade:
        data_table.add_rows([i])
    print(data_table)

# menu utama
def show_menu():
    clear()
    print("=======================================================")
    print("=   Hasil Akhir Nilai Mata Kuliah Bahasa Indonesia    =")
    print("=======================================================")
    print("= 1. Tampil Data                                      =")
    print("= 2. Cari Data                                        =")
    print("= 3. Nilai Tertinggi                                  =")
    print("= 4. Nilai Terendah                                   =")
    print("= 5. Rata - Rata                                      =")
    print("= 6. Keluar                                           =")
    print("=======================================================")
    pilihan = input("Masukkan pilihan : ")
    return pilihan

# kemnbali ke menu
def back_menu():
    print("\n")
    input("Tekan enter untuk kembali...")
    entry_point()

# entry point program
def entry_point():
    while True:
        pilihan = show_menu()
        if (pilihan == "1"): # pilihan pertama tampilkan seluruh data
            clear()
            show_data(total_grade)
            back_menu()
        elif (pilihan == "2"): # pilihan kedua cari data berdasarkan nama
            clear()
            key = input("Masukkan nama : ") # key pencarian
            cari = list(filter(lambda x: x if x[1] == key else False, total_grade)) # cari berdasarkan elemen ke-1
            show_data(cari)
            back_menu()
        elif (pilihan == "3"): # cari nilai maksimum data, tampilkan nama dan nilai
            clear()
            maximum_val = max(total_grade, key=lambda x: x[0])  # cari nilai maksimum berdasarkan elemen ke-0
            maximum_val = [maximum_val]
            print("=========== nilai tertinggi ============")
            show_data(maximum_val)
            back_menu()
        elif (pilihan == "4"): # cari nilai minimum data, tampilkan nama dan nilai
            clear()
            minimum_val = min(total_grade, key=lambda x: x[0])  # cari nilai minimum berdasarkan elemen ke-0
            minimum_val = [minimum_val]
            show_data(minimum_val)
            back_menu()
        elif (pilihan == "5"): # cari nilai rata-rata semua data
            clear()
            table_rerata = PrettyTable()
            table_rerata.field_names = ['Rata - rata']
            rerata = lambda x, y: x / y # cari rata-rata
            rerata = round(rerata(jumlah, 48), 2)
            table_rerata.add_row([rerata])
            print(table_rerata)
            back_menu()
        elif(pilihan == "6"): # keluar dari program
            print("Program keluar")
            exit()
        else:
            print("Pilihan tidak tersedia") # jika pilihan tidak tersedia
            back_menu()

entry_point()