# units = {
#     0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dörd", 5: "beş",
#     6: "altı", 7: "yeddi", 8: "səkkiz", 9: "doqquz"
# }

# tens = {
#     10: "on", 20: "iyirmi", 30: "otuz", 40: "qırx", 50: "əlli",
#     60: "altmış", 70: "yetmiş", 80: "səksən", 90: "doxsan"
# }

# def number_to_text(n):
#     n = int(n)
#     if n == 0:
#         return "sıfır"
#     words = []

#     # Onluqlar
#     if n >= 10:
#         t = (n // 10) * 10
#         words.append(tens[t])
#         n %= 10

#     # Təkliklər
#     if n > 0:
#         words.append(units[n])

#     return " ".join(words)

# while True:
#     x = input("Rəqəm daxil edin (çıqmaq üçün s): ")
#     if x.lower() == "s":
#         break
#     if not x.isdigit():
#         print("Yalnız rəqəm yazın!")
#         continue

#     print("→", number_to_text(x))



def cemi(n):
    if n < 10:
        return n
    
    cem = 0
    for reqem in str(n):
    
        cem += int(reqem)
    
    return cemi(cem)

eded = 146
netice = cemi(eded)
print("Nəticə:", netice)

