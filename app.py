import random
from country_list import get_countries

countries = get_countries()
# print(countries)

generalt_szo = random.choice(countries)

print(generalt_szo)

mondott_betu = input("Adj meg egy betűt! ")

if mondott_betu in generalt_szo:
    print("yes")
else:
    print("nah")