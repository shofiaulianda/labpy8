nilai = [80, 90, 'A', 70, 100, 90, 'B']

total = 0
jumlah_valid = 0

for data in nilai:
    try:
        # Coba tambahkan nilai
        total += data
        jumlah_valid += 1
    except TypeError:
        # Jika bukan angka, skip
        print(f"Data tidak valid dilewati: {data}")

# Hitung rata-rata dari data valid saja
if jumlah_valid > 0:
    rata_rata = total / jumlah_valid
    print("\nJumlah data valid :", jumlah_valid)
    print("Rata-rata nilai    :", rata_rata)
else:
    print("Tidak ada data valid untuk dihitung.")