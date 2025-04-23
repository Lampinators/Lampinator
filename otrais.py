print("Ievadi 2 skaitlus")
pirmais = int(input())
otrais = int(input())
print(pirmais + otrais)
reizes = 1.0
reizes = pirmais / otrais
if pirmais > otrais:
    print("Pirmais lielāks nekā otrais par", pirmais - otrais, "jeb", reizes, "reižu")
elif pirmais == otrais:
    print("Abi vienādi")
else:
    print("Otrais lielāks nekā pirmais par", otrais - pirmais, "jeb", reizes, "reižu")
