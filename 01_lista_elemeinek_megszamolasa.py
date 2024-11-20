"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

list = ['5', '8', '12', '15', '22']

print(len(list))

hossz = 1
for elem in list:
    hossz = hossz + 1

print(f"Lista elemei len methódussal: {len(list)}")
print(f"Lista elemei for methódussal: {hossz}")
    