import os
name=os.system(whoami)
print(f"merhaba {name} \n")
print("kütüphane yüklememize izin veriyor musunuz? \n")
print("ses modülü")
print("e/h deyin e evet, h hayır \n")
p=input("")
if p in ["E","e","Evet","evet"]:
  print("download")
  os.system(pip install playsound==1.2.2)
else:
  print("sesler yok")
print(f"{p} dediniz")
