print("Ievadi cilvēku sakitu!")
N = int(input())
print("Ievadi 1. autobusa ietilpību!")
A = int(input())
print("Ievadi 2. autobusa ietilpību!")
B = int(input())
print("Ievadi 2. autobusa ietilpību!")
C = int(input())
pilni_pari = N // (A + B + C)
atlikums = N% (A+B + C)
if atlikums == 0 :
    print("Vajag", pilni_pari, "A auto un ", pilni_pari, " B auto")
elif <= A :
    print("Vajag", pilni_pari + 1, "A auto un ", pilni_pari, " B auto")
else :
    print("Vajag", pilni_pari + 1, "A auto un ", pilni_pari + 1, " B auto")

