"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""
lista1 = [3, 1, 4]
lista2 = [9, 7, 2]

lista1.sort(reverse=False)
lista2.sort(reverse=False)
print(lista1+lista2)

# írasd ki az első és az utolsó elemet!