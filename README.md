# Pertemuan 11 - Dictionary/Map
Nama: Siti Nurjanah
NIM: 2225250110
Kelas: S1 Pendidikan Matematika - Semester 3

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Key utama yang digunakan adalah `NIM` mahasiswa. Value yang digunakan adalah dictionary bersarang yang memuat `nama`, `kelas`, dan `nilai`.

## Cara Menjalankan
python3 praktik/data_mahasiswa.py

## Test Case
| Input/Aksi | Hasil yang diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| A003 | Data Citra ditampilkan | Ditampilkan: {'nama': 'Citra', 'kelas': 'B', 'nilai': 92} | PASS |
| A999 | Pesan 'Data tidak ditemukan' | Ditampilkan 'Data tidak ditemukan' | PASS |
| A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Ditampilkan: 'nilai': 82 saat direkap | PASS |
| Tambah A006 | Key A006 tersedia setelah ditambahkan | Data Fajar tampil di rekap akhir | PASS |
| items() | Semua NIM dan data tampil | Seluruh 6 data tercetak berurutan | PASS |

## Refleksi
Satu kesalahan akses key yang ditemukan adalah munculnya `KeyError` saat mengakses key yang tidak ada. Cara memperbaikinya adalah menggunakan `.get()`.