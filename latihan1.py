print("=== Kalkulator Aman ===")

try:
    # Input angka pertama
    a = float(input("Masukkan angka pertama: "))

    # Input angka kedua
    b = float(input("Masukkan angka kedua: "))

    # Input operator
    op = input("Masukkan operator (+, -, *, /): ")

    # Cek operator valid
    if op not in ['+', '-', '*', '/']:
        raise Exception("Operator tidak valid! Gunakan salah satu: + - * /")

    # Perhitungan
    if op == '+':
        hasil = a + b
    elif op == '-':
        hasil = a - b
    elif op == '*':
        hasil = a * b
    elif op == '/':
        try:
            hasil = a / b
        except ZeroDivisionError:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
            exit()

    print(f"Hasil: {a} {op} {b} = {hasil}")

except ValueError:
    print("Error: Input harus berupa angka!")

except Exception as e:
    print("Error:", e)