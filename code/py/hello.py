import os

print("Kütüphane yüklememize izin veriyor musunuz? \n")
print("Ses modülü")
print("E/H deyin (E: Evet, H: Hayır) \n")

p = input("Seçiminiz: ")

if p in ["E", "e", "Evet", "evet"]:
    print("İndiriliyor...")
    # pip install kısmını da tırnak içine alıyoruz
    os.system("pip install playsound==1.2.2")
    print("Yükleme tamamlandı!")
else:
    print("Sesler devre dışı bırakıldı.")

print(f"'{p}' dediniz.")
