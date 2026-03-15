# Mövzu: siyahılar, lüğətlər, indeks və dəyər manipulyasiyası
N = 5
S = ['Riyaziyyat', 'Kimya', 'Fizika', 'Proqramlaşdirma', 'Cəbr']
T = {}
for i in range(len(S)):
 T[i+1]=S[i]
# "Proqramlaşdirma" açarını N ilə dəyiş
for key, value in T.items():
    if value == 'Proqramlaşdirma':
        T[N] = T.pop(key)
        break

print("T lüğəti:")
for k, v in T.items():
    print(k, ":", v)


# Mövzu: siyahılar, append, insert, sort
S1 = [1,3,5,7,9,11,13,15,17,19,21,23,25]
S2 = [30,40,50]
N2 = 99
N3 = 77
N = 3

S1.insert(0, N2)       # S1-in əvvəlinə N2 əlavə
S3 = S2 + S1
S3.insert(N-1, N3)     # S3-də N-ci yerə N3 əlavə
S3.sort(reverse=True)   # azalma sırası ilə düz

print("S3:", S3)




# Mövzu: datetime modulundan istifadə
from datetime import date, timedelta

birthday = date(2000, 1, 1)
N = 365
yenitarix = birthday + timedelta(days=N)
week_day = yenitarix.weekday()  # 0 = Bazar ertəsi, 6 = Bazar günü

print("Gələcək tarix:", yenitarix)
print("Həftənin günü (0=Mon):", week_day)
