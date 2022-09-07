from calendar import c
from tkinter import Y


list_integer = [1, 2, 3, 10, 200, 250]
list_string = ["Naufal", "icak", "akmal", "zaky"]
list_mix = [50, "zakiy", True, "ucup"]

print("data sebelum diubah:", list_string)
list_string[0] = "putra"
print("data setelah diubah:", list_string)

print("data sebelum diubah:", list_string)
list_string[2] = "Abizar"
print("data setelah diubah:",  list_string)


print("data sebelum diubah:", list_mix)
list_mix[0] = 100
print("data setelah diubah:", list_mix)

print("data sebelum diubah:", list_mix)
list_mix[1] = "abyan"
print("data setlah diubah:", list_mix)

print("data sebelum diubah:", list_mix)
list_mix[2] = "False"
print("data setelah diubah:", list_mix)

print("data sebelum diubah:", list_mix)
list_mix[3] = "angga"
print("data setelah diubah:", list_mix)
    
 # Perulangan for

x = ["Naufal", "icak", "akmal", "luntung"]    
for y in x:
    print(y)

    print("\n")
    for i in list_string:
       print(i)

K = [50, "zakiy", True, "ucup"]
for f in K:
    print(f)

    print("\n")

    for d in list_mix:
        print(d)