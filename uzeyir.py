# # # # mehsullar = [
# # # #     {"ad": "Qələm", "qiymet": 1.0, "say": 50},
# # # #     {"ad": "Dəftər", "qiymet": 2.5, "say": 30},
# # # #     {"ad": "Pozan", "qiymet": 0.8, "say": 40}
# # # # ]

# # # # for mehsul in mehsullar:
# # # #     mehsul["qiymet"] = mehsul["qiymet"] * 1.10

# # # # for mehsul in mehsullar:
# # # #     print("Məhsul:", mehsul["ad"],"Qiymət:", mehsul["qiymet"])


# # # herf1 = input("Birinci hərfi daxil edin: ")
# # # herf2 = input("İkinci hərfi daxil edin: ")

# # # kod1 = ord(herf1)
# # # kod2 = ord(herf2)

# # # orta_kod = (kod1 + kod2) // 2
# # # orta_herf = chr(orta_kod)

# # # print("Aradakı hərf:", orta_herf)



# # def abreviatura_yarat(ifade):
# #     sozler = ifade.split()  
# #     netice = ""

# #     for soz in sozler:
# #         netice = netice + soz[0].upper()  

# #     return netice


# # metn = input("İfadəni daxil edin: ")
# # print("Abreviatura:", abreviatura_yarat(metn))

# # Riyazi hesablamalar üçün funksiyalar (modul kimi)

# # def toplama(a, b):
# #     return a + b

# # def cixma(a, b):
# #     return a - b

# # def vurma(a, b):
# #     return a * b

# # def bolme(a, b):
# #     return a / b

# # print("Toplama:", toplama(5, 3))
# # print("Çıxma:", cixma(10, 4))
# # print("Vurma:", vurma(6, 2))
# # print("Bölmə:", bolme(8, 2))


# # Müstəvi fiqurların sahəsini hesablayan funksiyalar (modul kimi)

# # def kvadrat_sahesi(teref):
# #     return teref * teref

# # def duzbucaqli_sahesi(en, uzunluq):
# #     return en * uzunluq

# # def ucbucaq_sahesi(oturacaq, hundurluk):
# #     return (oturacaq * hundurluk) / 2

# # def daire_sahesi(radius):
# #     pi = 3.14
# #     return pi * radius * radius

# # print("Kvadratın sahəsi:", kvadrat_sahesi(4))
# # print("Düzbucaqlının sahəsi:", duzbucaqli_sahesi(3, 5))
# # print("Üçbucağın sahəsi:", ucbucaq_sahesi(6, 4))
# # print("Dairənin sahəsi:", daire_sahesi(2))

# # metn = input("Mətni daxil edin: ")

# # netice = ""

# # for herf in metn:
# #     if herf == 'z':
# #         netice = netice + 'a'
# #     else:
# #         yeni_herf = chr(ord(herf) + 3)
# #         netice = netice + yeni_herf

# # print("Şifrələnmiş mətn:", netice)


# # siyahi = [1, "a", 3, "ab", 5, "z", 7]

# # yeni_siyahi = []

# # for element in siyahi:
# #     if type(element) == int:  
# #         yeni_siyahi.append(element)

# # print("Ancaq ədədlər:", yeni_siyahi)


# # siyahi = [5, -3, 7, -1, 0, 8, -6]

# # yeni_siyahi = []

# # for eded in siyahi:
# #     if eded >= 0:  
# #         yeni_siyahi.append(eded)

# # print("yeni:", yeni_siyahi)

# import random
# import string

# print("🔐 Professional Password Generator")

# length = int(input("Uzunluq: "))

# use_upper = input("Böyük hərf olsun? (b/x): ")
# use_digits = input("Rəqəm olsun? (b/x): ")
# use_symbols = input("Simvol olsun? (b/x): ")

# characters = string.ascii_lowercase

# if use_upper == "b":
#     characters += string.ascii_uppercase

# if use_digits == "b":
#     characters += string.digits

# if use_symbols == "b":
#     characters += string.punctuation

# password = "".join(random.choice(characters) for i in range(length))

# print("Şifrə:", password)





