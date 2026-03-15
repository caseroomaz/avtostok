
# # N = 25  # nümunə üçün 20-50 arasında ədəd
# # siyahi = list(range(N + 1))
# # M = 17  # misal olaraq çatışmayan ədəd

# # inverse = -(M+1)               # M-in inversiyası
# # sola = M << 2         # M-in 2 vahid sola sürüşməsi
# # saga = M >> 2        # M-in 2 vahid sağa sürüşməsi

# # print("M:", M)
# # print("Inversiya:", inverse)
# # print("sola:", sola)
# # print("saga:", saga)

# # Mövzu: çoxluqlar, set əməliyyatları
# # import random

# # N = 50
# # S1 = set(random.sample(range(1, N+1), 10))
# # S2 = set(random.sample(range(1, N+1), 10))

# # kesisme = S1 & S2
# # birlesme = S1 | S2
# # ferq = S1 - S2
# # simmetrikferq = S1 ^ S2

# # print("S1:", S1)
# # print("S2:", S2)
# # print("Kəsişmə:", kesisme)
# # print("Birləşmə:", birlesme)
# # print("Fərq:", ferq)
# # print("Simmetrik fərq:", simmetrikferq)

# # # Birləşmədə 15 element varsa, onu sil
# # if 15 in birlesme:
# #     birlesme.remove(15)
# # print("Birləşmə (15 silindikdən sonra):", birlesme)

# # Mövzu: lüğətlər, ternar operator
# N = 85
# ballar = {'Riyaziyyat': 90, 'Kimya': 80, 'Fizika': 88}
# ortabal = sum(ballar.values()) / len(ballar)
# K = "Yaxşı nəticə" if ortabal > N else "Pis deyil"

# print("Orta bal:", ortabal)
# print("Qiymətləndirmə:", K)  

# # Mövzu: dövr operatorları, list, riyazi əməliyyatlar
# N = 14
# fib = [1, 1]
# for i in range(2, N):
#     fib.append(fib[i-1] + fib[i-2])

# fib_N = fib[N-1]
# qızılnısbet = fib[N-1] / fib[N-2]

# print(f"{N}-ci Fibonacci ədədi:", fib_N)
# print("Qızıl nisbət:", qızılnısbet)

# nums = [10, 20, 30, 40, 15, 25]
# N = 45

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == N:
#             print("Ədədlər:", nums[i], nums[j])
#             print("İndekslər:", i, j)


N = 8

S = ['Riyaziyyat', 'Kimya', 'Fizika', 'Proqramlaşdirma', 'Cəbr']

# Lüğət yaratmaq
T = {}
for i in range(len(S)):
    T[i + 1] = S[i]

# "Proqramlaşdirma" açarını N ilə əvəz etmək
for key, value in list(T.items()):
    if value == "Proqramlaşdirma":
        T[N] = T.pop(key)

# Ekrana çıxarış
for k, v in T.items():
    print(k, ":", v)
