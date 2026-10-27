def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)
if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

nim_kosong = "A999"
hasil_kosong = cari_mahasiswa(data_mahasiswa, nim_kosong)
if hasil_kosong is not None:
    print(f"{nim_kosong}: {hasil_kosong}")
else:
    print("Data tidak ditemukan")

data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

data_mahasiswa["A002"]["nilai"] = 82

print("\nRekap Data Mahasiswa:")
for nim_mhs, info in data_mahasiswa.items():
    print(nim_mhs, info)

print(f"\nRata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")