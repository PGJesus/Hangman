import random
from country_list import get_countries

countries = get_countries()
# print(countries)

generalt_szo = random.choice(countries)
nemtalalatok = 0
print(generalt_szo)

betu_szam = len(generalt_szo)
for betu in generalt_szo:
    print("_ ")

    if " " in generalt_szo:
        print(" ")


mondott_betu = input("Adj meg egy betűt! ")

if mondott_betu in generalt_szo:
    print("yes")
else:
    print("nah")
    nemtalalatok += 1

print(nemtalalatok)