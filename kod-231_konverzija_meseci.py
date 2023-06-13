# jan -> Januar
# ako ne postoji kljuc, stampati predefinisanu poruku

konverzija_meseci = {
    "jan":"Januar",
    "feb":"Februar",
    "mar":"Mart",
    "apr":"April",
    "maj":"Maj",
    "jun":"Jun",
    "jul":"Jul",
    "avg":"Avgust",
    "sep":"Septembar",
    "okt":"Oktobar",
    "nov":"Novembar",
    "dec":"Decembar"
}

print(konverzija_meseci)
# print(konverzija_meseci.keys())
# print(konverzija_meseci.values())
print(konverzija_meseci["avg"])
print(konverzija_meseci["jul"])
print(konverzija_meseci.get("lim", "Mesec Limburg"))