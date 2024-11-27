import requests

#část 1 
ico = input("Zadej číslené IČO subjektu, který tě zajímá:").strip()
response = requests.get("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico)
vystup = response.json()
#print(vystup.keys())
if response.status_code == 200:
    print(vystup["obchodniJmeno"])
    print(vystup["sidlo"]["textovaAdresa"])
else:
    print("Zadané ičo nebylo nalezeno")

#část 2
nazev = input("Zadej název subjektu:").strip()
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno": "' + nazev +'"}'
data = data.encode("utf-8")
response_2 = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers = headers, data = data)
vystup_2 = response_2.json()
#print(vystup_2.keys())
pocet_subjektu = vystup_2["pocetCelkem"]
print(f"Nalezeno subjektů: {pocet_subjektu}")
for i in range(pocet_subjektu):
    print(f"{vystup_2["ekonomickeSubjekty"][i]["obchodniJmeno"]}, {vystup_2["ekonomickeSubjekty"][i]["ico"]}")
