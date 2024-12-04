data_panen = {
    'lokasi1': {
        'nama_lokasi': 'kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }    
    }
}

for l, data in data_panen.items():
    print(f"Lokasi: {l}")
    print(f"Nama Lokasi: {data['nama_lokasi']}")
    print("Hasil Panen:")
    for k, jumlah in data['hasil_panen'].items():
        print(f"  {k}: {jumlah}")
    print()

jl2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari lokasi2: {jl2}\n")

nl3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nl3}\n")

pp = {}
pk = {}

for l, detail in data_panen.items():
    pp[l] = detail['hasil_panen']['padi']
    pk[l] = detail['hasil_panen']['kedelai']

print("\nHasil Panen Padi Setiap Lokasi:")
print(pp)

print("\nHasil Panen Kedelai Setiap Lokasi:")
print(pk)

print("\nStatus Lokasi:")
for l, detail in data_panen.items():
    p = detail['hasil_panen']['padi']
    j = detail['hasil_panen']['jagung']
    
    if p > 1300 or j > 800:
        print(f"{l} ({detail['nama_lokasi']}): Memerlukan Perhatian Khusus")
    else:
        print(f"{l} ({detail['nama_lokasi']}): Dalam Kondisi Baik")

print("Farras Abdillah")
print("152023097")