# def reqem_cemi(n):
#     # Ədəd mənfi olarsa müsbətə çeviririk
#     n = abs(n)

#     # Birrəqəmli ədəd alınanda dayanırıq (baz hal)
#     if n < 10:
#         return n

#     # Rəqəmlərin cəmini hesablayırıq
#     cem = 0
#     while n > 0:
#         cem += n % 10
#         n //= 10

#     # Rekursiv olaraq funksiyanı yenidən çağırırıq
#     return reqem_cemi(cem)


# # İstifadəçi daxil edilməsi
# eded = int(input("Ədəd daxil edin: "))
# netice = reqem_cemi(eded)0


# print(f"Nəticə: {netice}")






# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(8))






def cem(n):
    cemi=0
    for reqem in str(n):
        cemi=cemi +  int(reqem)
        if cemi < 10:
            return cemi 
        else:
            return cem(cemi)
print(cem(987))        
    